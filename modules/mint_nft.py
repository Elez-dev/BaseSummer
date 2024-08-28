from modules.wallet import Wallet
from loguru import logger
from modules.retry import exception_handler
from eth_account.messages import encode_defunct
from web3 import Web3
import json as js
from datetime import datetime
import ua_generator
import requests


class MintNFT(Wallet):
    def __init__(self, private_key, chain, number, proxy):
        super().__init__(private_key, chain, number, proxy)
        self.address = Web3.to_checksum_address('0x1d6b183bd47f914f9f1d3208edcf8befd7f84e63')
        self.abi = js.load(open('./abi/coin_earnings.txt'))
        self.contract = self.web3.eth.contract(address=self.address, abi=self.abi)

    @exception_handler('Mint BASE PYTHON ZORB')
    def mint_python_zorb_base_opensea(self):
        logger.info('Mint BASE PYTHON ZORB')

        dick = {
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            **self.get_gas_price()
        }

        contract = self.web3.eth.contract(address=Web3.to_checksum_address('0x00005ea00ac477b1030ce78506496e8c2de24bf5'), abi=js.load(open('./abi/opensea.txt')))
        txn = contract.functions.mintPublic(
            Web3.to_checksum_address('0x92dFC144B8B897d36E980e6E29217201801A1C1e'),
            Web3.to_checksum_address('0x0000a26b00c1F0DF003000390027140000fAa719'),
            Web3.to_checksum_address('0x0000000000000000000000000000000000000000'),
            1
        ).build_transaction(dick)

        self.send_transaction_and_wait(txn, f'Mint BASE PYTHON ZORB on OpenSea')

    @exception_handler('Mint web app')
    def mint_web_app(self):
        contract = self.web3.eth.contract(
            address=Web3.to_checksum_address('0x6B033e8199ce2E924813568B716378aA440F4C67'),
            abi=js.load(open('./abi/abi2.txt')))
        name = contract.functions.name().call()
        if contract.functions.balanceOf(self.address_wallet).call() > 0:
            logger.info(f'NFT {name} already minted\n')
            return False

        data = f'0x84bb1e42000000000000000000000000{self.address_wallet[2:]}0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee00000000000000000000000000000000000000000000000000005af3107a400000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001800000000000000000000000000000000000000000000000000000000000000080ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00000000000000000000000000000000000000000000000000005af3107a4000000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001d4da48b00000000'
        txn = {
            'chainId': self.web3.eth.chain_id,
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'to': Web3.to_checksum_address('0x6B033e8199ce2E924813568B716378aA440F4C67'),
            'value': Web3.to_wei(0.0001, 'ether'),
            'data': data,
            **self.get_gas_price()
        }

        txn.update({'gas': self.web3.eth.estimate_gas(txn)})

        self.send_transaction_and_wait(txn, f'Mint {name} successfully')

    @exception_handler('Mint team liquid')
    def mint_liquid(self):
        contract = self.web3.eth.contract(
            address=Web3.to_checksum_address('0x1b9Ac8580d2E81d7322f163362831448E7FcAD1B'),
            abi=js.load(open('./abi/abi2.txt')))
        name = contract.functions.name().call()
        if contract.functions.balanceOf(self.address_wallet).call() > 0:
            logger.info(f'NFT {name} already minted\n')
            return False

        data = f'0x84bb1e42000000000000000000000000{self.address_wallet[2:]}0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000180000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000021fb3f'
        txn = {
            'chainId': self.web3.eth.chain_id,
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'to': Web3.to_checksum_address('0x1b9ac8580d2e81d7322f163362831448e7fcad1b'),
            'data': data,
            **self.get_gas_price()
        }

        txn.update({'gas': self.web3.eth.estimate_gas(txn)})

        self.send_transaction_and_wait(txn, f'Mint {name} successfully')

    @exception_handler('Mint mister migless')
    def mint_mister_migless(self):
        contract = self.web3.eth.contract(
            address=Web3.to_checksum_address('0xDc03a75F96f38615B3eB55F0F289d36E7A706660'),
            abi=js.load(open('./abi/abi3.txt')))
        name = contract.functions.name().call()
        if contract.functions.balanceOf(self.address_wallet, 0).call() > 0:
            logger.info(f'NFT {name} already minted\n')
            return False

        data = f'0x760f2a0b000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000020000000000000000000000000849ef788b40af342e2883c3112dd636f03a4203e00000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000b5e620f480000000000000000000000000000000000000000000000000000000000000000484b510391f000000000000000000000000{self.address_wallet[2:]}00000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000404e8d51ef50000000000000000000000000000000000000000000000000000000000000060000000000000000000000000{self.address_wallet[2:]}000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000020000000000000000000000000dc03a75f96f38615b3eb55f0f289d36e7a70666000000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000005af3107a400000000000000000000000000000000000000000000000000000000000000002e0000000000000000000000000dc03a75f96f38615b3eb55f0f289d36e7a7066600000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000034000000000000000000000000000000000000000000000000000000000000001c457bc3d78000000000000000000000000{self.address_wallet[2:]}00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee00000000000000000000000000000000000000000000000000005af3107a400000000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000001a00000000000000000000000000000000000000000000000000000000000000080ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00000000000000000000000000000000000000000000000000005af3107a4000000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000055c88bb05602da94fce8feadc1cbebf5b72c245300000000000000000000000000000000000000000000000000005af3107a4000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001d4da48b00000000'
        txn = {
            'chainId': self.web3.eth.chain_id,
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'to': Web3.to_checksum_address('0x1aeD60A97192157fDA7fb26267A439d523d09c5e'),
            'value': Web3.to_wei(0.0002, 'ether'),
            'data': data,
            **self.get_gas_price()
        }

        txn.update({'gas': self.web3.eth.estimate_gas(txn)})

        self.send_transaction_and_wait(txn, f'Mint {name} successfully')

    @exception_handler('Mint onchain summer nft')
    def mint_base_summer_nft(self, nft_number):
        address = [
            '0x615194d9695d0c02Fc30a897F8dA92E17403D61B',  # EURC x Base Launch
            '0xb5408b7126142C61f509046868B1273F96191b6d',  # Celebrating the Ethereum ETF
            '0xE65dFa5C8B531544b5Ae4960AE0345456D87A47D',  # Happy Birthday Toshi
            '0x96E82d88c07eCa6a29B2AD86623397B689380652',  # ETH BREAKING THROUGH
            '0xb0FF351AD7b538452306d74fB7767EC019Fa10CF',  # ETH can&#39;t be stopped
            '0x955FdFdFd783C89Beb54c85f0a97F0904D85B86C',  # the world after ETH ETF approval
            '0xC00F7096357f09d9f5FE335CFD15065326229F66',  # Ethereum ETF
            '0xE8aD8b2c5Ec79d4735026f95Ba7C10DCB0D3732B',  # ETFEREUM
            '0xbFa3fF9dcdB811037Bbec89f89E2751114ECD299',  # Toshi Vibe
            '0x2382456097cC12ce54052084e9357612497FD6be',  # Stand With Crypto | Song A Day #5714
            '0x4beAdC00E2A6b6C4fAc1a43FF340E5D71CBB9F77',  # Stand with Crypto Pizza
            '0x4e4431BDdC2a896b1268ded02807b78c318C82e0',  # Endaoment X SWC
            '0x146B627a763DFaE78f6A409CEF5B8ad84dDD4150',  # Stand with Crypto
            '0x9FF8Fd82c0ce09caE76e777f47d536579AF2Fe7C',  # strut 001
            '0x651b0A2b9FB9C186fB6C9a9CEddf25B791Ad5753',  # Crypto will bloom
            '0xea50e58B518435AD2CeCE84d1e099b2e0878B9cF',  # What if we added a S
            '0x6a43B7e3ebFc915A8021dd05f07896bc092d1415',  # Crypto Vibe(CV)
            '0x892Bc2468f20D40F4424eE6A504e354D9D7E1866',  # The Creative Shield
            '0xb620bEdCe2615A3F35273A08b3e45e3431229A60',  # Toshi x SWC 3
            '0x5b45498D20d24D9c6Da165eDcd0eBcE0636176Ae',  # duality in motion
            '0x1f006edBc0Bcc528A743ee7A53b5e3dD393A1Df6',  # en garde
            '0x279dFFD2b14a4A60e266bEfb0D2c10E695D58113',  # Live and Let Live!
            '0x8605522B075aFeD48f9987E573E0AA8E572B8452',  # Mint the vision
            '0x13fCcd944B1D88d0670cae18A00abD272256DDeE',  # Stand With Crypto Shield Rune
            '0x6A3dA97Dc82c098038940Db5CB2Aa6B1541f2ebe',  # Shielding the wonder
            '0xd1E1da0b62761b0df8135aE4e925052C8f618458',  # Earth Stands with Crypto
            '0x03c6eF731453bfEc65a800F83f026ad011D8Abec',  # ⌐◨-◨ Stand With Crypto
            '0xEb9A3540E6A3dc31d982A47925d5831E02a3Fe1e',  # we stand, we build
            '0x2a8e46E78BA9667c661326820801695dcf1c403E',  # Let The Shield Shine
            '0x8e50c64310b55729F8EE67c471E052B1Cd7AF5b3',  # All for One
            '0x95ff853A4C66a5068f1ED8Aaf7c6F4e3bDBEBAE1'  # Even Sam Stands with Crypto
        ]

        dick = {
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'value': Web3.to_wei(0.0001, 'ether'),
            **self.get_gas_price()
        }

        if nft_number == 21:
            dick.update({'value': Web3.to_wei(0.0005, 'ether')})

        contract = self.web3.eth.contract(
            address=Web3.to_checksum_address(address[nft_number]),
            abi=js.load(open('./abi/abi1.txt')))
        name = contract.functions.name().call()
        if contract.functions.balanceOf(self.address_wallet).call() > 0:
            logger.info(f'NFT {name} already minted\n')
            return False
        txn = contract.functions.mintWithComment(
            self.address_wallet,
            1,
            ''
        ).build_transaction(dick)

        self.send_transaction_and_wait(txn, f'Mint {name} successfully')

    @exception_handler('Mint smart wallet nft')
    def mint_smart_wallet(self):
        txn = {
            'chainId': self.web3.eth.chain_id,
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'to': Web3.to_checksum_address('0x76c7104567b5D32D4B084C8034724f9103F285be'),
            'data': f'0x84bb1e42000000000000000000000000{self.address_wallet[2:]}0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001800000000000000000000000000000000000000000000000000000000000000080ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000021fb3f',
            **self.get_gas_price()
        }

        txn.update({'gas': self.web3.eth.estimate_gas(txn)})

        self.send_transaction_and_wait(txn, f'Mint Introducing Smart Wallet successfully')

    @exception_handler('Mint Buildathon')
    def mint_buildathon(self):
        contract = self.web3.eth.contract(
            address=Web3.to_checksum_address('0x0c45CA58cfA181b038E06dd65EAbBD1a68d3CcF3'),
            abi=js.load(open('./abi/abi1.txt')))
        name = contract.functions.name().call()
        if contract.functions.balanceOf(self.address_wallet).call() > 0:
            logger.info(f'NFT {name} already minted\n')
            return False

        txn = {
            'chainId': self.web3.eth.chain_id,
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'to': Web3.to_checksum_address('0x0c45CA58cfA181b038E06dd65EAbBD1a68d3CcF3'),
            'value': Web3.to_wei(0.0001, 'ether'),
            'data': f'0x84bb1e42000000000000000000000000{self.address_wallet[2:]}0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee00000000000000000000000000000000000000000000000000005af3107a400000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001800000000000000000000000000000000000000000000000000000000000000080ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00000000000000000000000000000000000000000000000000005af3107a4000000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001d4da48b00000000',
            **self.get_gas_price()
        }

        txn.update({'gas': self.web3.eth.estimate_gas(txn)})

        self.send_transaction_and_wait(txn, f'Mint Buildathon successfully')

    def get_nonce(self):
        url = 'https://gram.voyage/api/ocs/nonce'
        data = self.get_api_call_data_get(url)
        return data['data']['nonce']

    def get_token(self):
        issued_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
        nonce = self.get_nonce()
        url = 'https://gram.voyage/api/ocs/verify'
        text = f'gram.voyage wants you to sign in with your Ethereum account:\n'\
               f'{self.address_wallet}\n\n'\
               f'Sign in Grampus.\n\n'\
               f'URI: https://gram.voyage\n'\
               f'Version: 1\n'\
               f'Chain ID: 8453\n'\
               f'Nonce: {nonce}\n'\
               f'Issued At: {issued_at}'

        message = encode_defunct(text=text)
        signed_message = self.web3.eth.account.sign_message(message, self.private_key)
        signature = signed_message.signature
        json = {
            'message': {
                'address': self.address_wallet,
                'chainId': 8453,
                'domain': "gram.voyage",
                'issuedAt': issued_at,
                'nonce': nonce,
                'statement': 'Sign in Grampus.',
                'uri': 'https://gram.voyage',
                'version': '1'
            },
            'signature': Web3.to_hex(signature)
        }

        data = self.get_api_call_data_post(url, json)
        return data['data']['token']

    def get_data(self):
        url = 'https://gram.voyage/api/ocs/minting'
        ua = ua_generator.generate(device='desktop')
        headers = {
            'authorization': self.get_token(),
            'Origin': 'https://gram.voyage',
            'Referer': 'https://gram.voyage/game/juicyadventure',
            'Sec-Ch-Ua': ua.ch.brands,
            'Sec-Ch-Ua-Mobile': ua.ch.mobile,
            'Sec-Ch-Ua-Platform': ua.ch.platform,
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': ua.text
        }
        json = {
            'address': self.address_wallet,
            'nonce': 'd1d40b6fb16aa388',
            'order': [1, 2, 3]
        }
        with requests.Session() as s:
            response = s.post(url=url, json=json, timeout=5, headers=headers)
        data = response.json()
        token_id = data['data']['tokenId']
        rarity = data['data']['rarity']
        signature = data['data']['signature']
        return token_id, rarity, signature

    @exception_handler('Mint Juice Pack')
    def mint_juice(self):
        contract = self.web3.eth.contract(
            address=Web3.to_checksum_address('0x6ba5Ba71810c1196f20123B57B66C9ed2A5dBd76'),
            abi=js.load(open('./abi/juice.txt')))
        name = contract.functions.name().call()
        if contract.functions.balanceOf(self.address_wallet).call() > 0:
            logger.info(f'NFT {name} already minted\n')
            return False

        data = self.get_data()

        dick = {
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            **self.get_gas_price()
        }

        txn = contract.functions.mintJuicyPack(
            data[0],
            data[1],
            data[2]
        ).build_transaction(dick)
        self.send_transaction_and_wait(txn, f'Mint {name} successfully')

    @exception_handler('Mint Forbes Web3 INSPIRE')
    def mint_forbes(self):
        contract = self.web3.eth.contract(
            address=Web3.to_checksum_address('0x0821D16eCb68FA7C623f0cD7c83C8D5Bd80bd822'),
            abi=js.load(open('./abi/abi1.txt')))
        name = contract.functions.name().call()
        if contract.functions.balanceOf(self.address_wallet).call() > 0:
            logger.info(f'NFT {name} already minted\n')
            return False

        txn = {
            'chainId': self.web3.eth.chain_id,
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'to': Web3.to_checksum_address('0x0821D16eCb68FA7C623f0cD7c83C8D5Bd80bd822'),
            'data': f'0x84bb1e42000000000000000000000000{self.address_wallet[2:]}0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001800000000000000000000000000000000000000000000000000000000000000080ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001d4da48b00000000',
            **self.get_gas_price()
        }

        txn.update({'gas': self.web3.eth.estimate_gas(txn)})

        self.send_transaction_and_wait(txn, f'Mint {name} successfully')
