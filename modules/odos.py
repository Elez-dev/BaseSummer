import random
from web3 import Web3
import time
import requests
from modules.wallet import Wallet
from modules.retry import exception_handler
from settings import SLIPPAGE
from loguru import logger

odos_token = []


class OdosSwap(Wallet):

    """ https://app.odos.xyz/ """

    def __init__(self, private_key, chain, number, proxy):
        super().__init__(private_key, chain, number, proxy)
        self.proxy = proxy

    def get_data(self, token_from, token_to, value):
        url = 'https://api.odos.xyz/sor/quote/v2'
        json = {
            'chainId': 8453,
            'compact': True,
            'gasPrice': float(Web3.from_wei(self.web3.eth.gas_price, 'gwei')),
            'disableRFQs': False,
            'inputTokens': [{
                'amount': str(value),
                'tokenAddress': token_from
            }],
            'likeAsset': True,
            'outputTokens': [{
                'proportion': 1,
                'tokenAddress': token_to
            }],
            'pathViz': True,
            'referralCode': 1,
            'slippageLimitPercent': SLIPPAGE,
            'sourceBlacklist': [],
            'userAddr': self.address_wallet
        }

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'X-Sec-Fetch-Site': 'same-origin'
        }
        with requests.Session() as s:
            if self.proxy:
                s.proxies = self.proxy
            res = s.post(url=url, json=json, timeout=60, headers=header)
            if res.status_code >= 400:
                logger.error(f'{res.status_code} || Ошибка, скорее всего вы не включили впн или не добавили прокси\n')
                raise ValueError('')
        return res.json()

    def get_tx(self, path_id):
        url = 'https://api.odos.xyz/sor/assemble'
        json = {
            'pathId': path_id,
            'simulate': False,
            'userAddr': self.address_wallet
        }
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'X-Sec-Fetch-Site': 'same-origin'
        }
        with requests.Session() as s:
            if self.proxy:
                s.proxies = self.proxy
            res = s.post(url=url, json=json, timeout=60, headers=header)
        return res.json()

    @exception_handler('Buy token Odos')
    def buy_token(self, prescale):
        token_to_buy = random.choice(odos_token)
        token_contract = self.web3.eth.contract(address=token_to_buy, abi=self.token_abi)
        name = token_contract.functions.name().call()

        logger.info(f'Buy {name} token on Odos')
        balance = self.web3.eth.get_balance(self.address_wallet) - Web3.to_wei(0.00001, 'ether')
        if balance < 0:
            logger.error('Insufficient funds')
            return False
        value = int(balance * prescale)
        value_wei = Web3.from_wei(value, 'ether')

        token_from = {
            'address': '0x0000000000000000000000000000000000000000'
        }

        json_data = self.get_data(token_from, token_to_buy, value)

        min_tok = json_data['inValues'][0]
        path_id = json_data['pathId']

        json_data = self.get_tx(path_id)

        txn = {
            'chainId': 8453,
            'data': json_data['transaction']['data'],
            'from': self.address_wallet,
            'to': Web3.to_checksum_address(json_data['transaction']['to']),
            'value': int(json_data['transaction']['value']),
            'nonce': json_data['transaction']['nonce'],
            'gasPrice': self.web3.eth.gas_price
        }

        gas = self.web3.eth.estimate_gas(txn)
        txn.update({'gas': gas})

        self.send_transaction_and_wait(txn, f'Buy {min_tok} {name} Odos')

        return token_to_buy

    @exception_handler('Sold token Odos')
    def sold_token(self, token_to_sold):
        token_to_sold = Web3.to_checksum_address(token_to_sold)
        token_contract = self.web3.eth.contract(address=token_to_sold, abi=self.token_abi)
        name = token_contract.functions.name().call()
        decimal = token_contract.functions.decimals().call()
        logger.info(f'Sold {name} token on Odos')
        token_balance = token_contract.functions.balanceOf(self.address_wallet).call()
        if token_balance == 0:
            logger.error(f'Balance {name} - 0\n')
            return False
        token_to_buy = '0x0000000000000000000000000000000000000000'

        json_data = self.get_data(token_to_sold, token_to_buy, token_balance)

        min_tok = self.from_wei(decimal, token_balance)
        path_id = json_data['pathId']

        json_data = self.get_tx(path_id)

        spender = Web3.to_checksum_address(json_data['transaction']['to'])
        allowance = token_contract.functions.allowance(self.address_wallet, spender).call()
        if allowance < token_balance:
            logger.info('Need approve')
            self.approve(token_to_sold, spender)
            time.sleep(60)

        txn = {
            'chainId': 8453,
            'data': json_data['transaction']['data'],
            'from': self.address_wallet,
            'to': Web3.to_checksum_address(json_data['transaction']['to']),
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            **self.get_gas_price()
        }

        gas = self.web3.eth.estimate_gas(txn)
        txn.update({'gas': gas})

        self.send_transaction_and_wait(txn, f'Sold {min_tok} {name} Odos')
