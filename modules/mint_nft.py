from modules.wallet import Wallet
from loguru import logger
from modules.retry import exception_handler
from web3 import Web3
import json as js

abi = '''
[
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "txHash",
        "type": "bytes32"
      },
      {
        "internalType": "bytes",
        "name": "signature",
        "type": "bytes"
      }
    ],
    "name": "mint",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
'''


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
            '0x146B627a763DFaE78f6A409CEF5B8ad84dDD4150'   # Stand with Crypto
        ]

        dick = {
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'value': Web3.to_wei(0.0001, 'ether'),
            **self.get_gas_price()
        }

        if nft_number in range(13):
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

        if nft_number == 13:
            return self.mint_web_app()

        if nft_number == 14:
            return self.mint_liquid()

        if nft_number == 15:
            return self.mint_mister_migless()

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

    @exception_handler('Mint STIX Launch Tourname')
    def mint_stix(self):
        txn = {
            'chainId': self.web3.eth.chain_id,
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'to': Web3.to_checksum_address('0xa7891c87933BB99Db006b60D8Cb7cf68141B492f'),
            'data': f'0x84bb1e42000000000000000000000000{self.address_wallet[2:]}0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000180000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001d4da48b00000000',
            **self.get_gas_price()
        }

        txn.update({'gas': self.web3.eth.estimate_gas(txn)})

        self.send_transaction_and_wait(txn, f'Mint STIX Launch Tourname successfully')

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

        self.send_transaction_and_wait(txn, f'Mint STIX Launch Tourname successfully')

    @exception_handler('Mint WYWO')
    def mint_wywo(self):
        url = 'https://www.wishyouwereonchain.com/api/generate-signature'
        data = self.get_api_call_data_get(url)
        buffer = data['data']['buffer']
        signature = data['data']['signature']

        dick = {
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            **self.get_gas_price()
        }

        contract = self.web3.eth.contract(address=Web3.to_checksum_address('0x4242Dd24148dC0Cb58d3c802237dDb5C2bDaa735'), abi=abi)
        txn = contract.functions.mint(
            buffer,
            signature
        ).build_transaction(dick)

        self.send_transaction_and_wait(txn, f'Mint MPWishYouWereOnchain successfully')
