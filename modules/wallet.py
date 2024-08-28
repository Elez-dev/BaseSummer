import random
from web3 import Web3
import time
from web3.middleware import geth_poa_middleware
from requests.adapters import Retry
from modules.retry import exception_handler
import requests
from loguru import logger
from settings import CHAIN_RPC
from modules.tg_bot import TgBot
import ua_generator

SCAN = {
    'Base': 'https://basescan.org/tx/',
}


class Wallet(TgBot):

    def __init__(self, private_key, chain, number, proxies):
        self.private_key = private_key
        self.chain = chain
        self.number = number
        self.web3 = self.get_web3(chain)
        self.scan = self.get_scan(chain)
        self.account = self.web3.eth.account.from_key(private_key)
        self.address_wallet = self.account.address
        self.token_abi = [{'inputs': [{'internalType': 'string', 'name': '_name', 'type': 'string'}, {'internalType': 'string', 'name': '_symbol', 'type': 'string'}, {'internalType': 'uint256', 'name': '_initialSupply', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Approval', 'type': 'event'}, {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'from', 'type': 'address'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'Transfer', 'type': 'event'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'subtractedValue', 'type': 'uint256'}], 'name': 'decreaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'addedValue', 'type': 'uint256'}], 'name': 'increaseAllowance', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint8', 'name': 'decimals_', 'type': 'uint8'}], 'name': 'setupDecimals', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'internalType': 'address', 'name': 'recipient', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}]
        self.proxies = proxies
        self.session = requests.Session()
        self.set_proxy_and_headers()

    def set_proxy_and_headers(self):
        ua = ua_generator.generate(device='desktop')
        self.session.headers = {
            'Origin': 'https://wallet.coinbase.com',
            'Referer': 'https://wallet.coinbase.com/',
            'Sec-Ch-Ua': ua.ch.brands,
            'Sec-Ch-Ua-Mobile': ua.ch.mobile,
            'Sec-Ch-Ua-Platform': ua.ch.platform,
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': ua.text
        }

        if self.proxies:
            self.session.proxies = {
                'http': f'http://{self.proxies}',    # user:pass@ip:port
                'https': f'http://{self.proxies}',   # user:pass@ip:port
            }
            try:
                ip = self.session.get('https://ip.beget.ru/')
                logger.success(f'Proxy installed successfully, Your current ip - {ip.text}')
            except Exception as error:
                logger.error(f'Proxy not installed\n{error}')
                self.session.proxies = {}

    @staticmethod
    def get_web3(chain):
        retries = Retry(total=10, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        adapter = requests.adapters.HTTPAdapter(max_retries=retries)
        session = requests.Session()
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return Web3(Web3.HTTPProvider(CHAIN_RPC[chain], request_kwargs={'timeout': 60}, session=session))

    @staticmethod
    def get_web3_refuel(chain):
        retries = Retry(total=10, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        adapter = requests.adapters.HTTPAdapter(max_retries=retries)
        session = requests.Session()
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return Web3(Web3.HTTPProvider(CHAIN_RPC[chain], request_kwargs={'timeout': 60}, session=session))

    @staticmethod
    def get_scan(chain):
        return SCAN[chain]

    @staticmethod
    def to_wei(decimal, amount):
        if decimal == 6:
            unit = 'picoether'
        else:
            unit = 'ether'

        return Web3.to_wei(amount, unit)

    @staticmethod
    def from_wei(decimal, amount):
        if decimal == 6:
            unit = 'picoether'
        elif decimal == 8:
            return float(amount / 10 ** 8)
        else:
            unit = 'ether'

        return Web3.from_wei(amount, unit)

    def approve(self, token_to_approve, address_to_approve):
        token_contract = self.web3.eth.contract(address=token_to_approve, abi=self.token_abi)
        max_amount = 2 ** 256 - 1
        dick = {
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            **self.get_gas_price()
        }
        txn = token_contract.functions.approve(address_to_approve, max_amount).build_transaction(dick)

        self.send_transaction_and_wait(txn, 'approve')

    def send_transaction_and_wait(self, tx, message):
        signed_txn = self.web3.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        logger.info('Sent a transaction')
        time.sleep(5)
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash, timeout=900, poll_latency=5)
        if tx_receipt.status == 1:
            logger.success('The transaction was successfully mined')
        else:
            logger.error("Transaction failed, I'm trying again")
            self.send_message_error(self.number, message, self.address_wallet, "Transaction failed, I'm trying again")
            raise ValueError('')

        self.send_message_success(self.number, message, self.address_wallet, f'{self.scan}{tx_hash.hex()}')

        logger.success(f'[{self.number}] {message} || {self.scan}{tx_hash.hex()}\n')
        return tx_hash

    def get_native_balance(self):
        return self.web3.eth.get_balance(self.address_wallet)

    def get_gas_price(self):
        if self.chain in ["Polygon", "Avax", 'Zora']:
            try:
                self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
            except: pass

        return {'maxFeePerGas': int(self.web3.eth.gas_price * 1.1), 'maxPriorityFeePerGas': int(self.web3.eth.gas_price * 0.1)}

    def get_api_call_data_post(self, url, json):
        call_data = self.session.post(url, json=json, timeout=60)
        api_data = call_data.json()
        return api_data

    def get_api_call_data_get(self, url):
        call_data = self.session.get(url, timeout=60)
        if call_data.status_code < 400:
            api_data = call_data.json()
            return api_data
        else:
            logger.error("Couldn't get a response")
            raise ValueError('')

    @exception_handler('Transfer ETH')
    def transfer_native(self, address, value=None):

        balance = self.get_native_balance()
        if balance - Web3.to_wei(0.00005, 'ether') <= 0:
            logger.error(f'Balance ETH < 0.00005\n')
            return

        if value is None:
            max_value = balance - Web3.to_wei(0.00005, 'ether')
            min_value = int(balance / 100)
            value = round(Web3.from_wei(random.randint(min_value, max_value), 'ether'), 6)

        amount = Web3.to_wei(value, 'ether')

        dick = {
            'chainId': self.web3.eth.chain_id,
            'from': self.address_wallet,
            'to': Web3.to_checksum_address(address),
            'value': amount,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'gas': 21_000,
            **self.get_gas_price()
        }

        self.send_transaction_and_wait(dick, f'Transfer {Web3.from_wei(amount, "ether")} ETH to {address}')
