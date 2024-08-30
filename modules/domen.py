import time
import random
from modules.wallet import Wallet
from loguru import logger
from modules.retry import exception_handler
from web3 import Web3
import json as js
from eth_utils import keccak
from hexbytes import HexBytes
from eth_utils import to_hex
from eth_abi import encode
from mimesis import Person


class Domen(Wallet):
    def __init__(self, private_key, chain, number, proxy):
        super().__init__(private_key, chain, number, proxy)
        self.address = Web3.to_checksum_address('0x4cCb0BB02FCABA27e82a56646E81d8c5bC4119a5')
        self.abi = js.load(open('./abi/domen.txt'))
        self.contract = self.web3.eth.contract(address=self.address, abi=self.abi)
        self.address_validator = Web3.to_checksum_address('0x9de4Ab12320684cec803Edb72aA3a920250d392C')

    @staticmethod
    def namehash(name):
        node = HexBytes('0x' + '00' * 32)  # Начальное значение для хэша пустого домена
        if name:
            labels = name.split(".")
            for label in reversed(labels):
                label_hash = keccak(text=label)
                node = keccak(node + label_hash)
        return node

    @staticmethod
    def add_random_digits(s):
        digit1 = str(random.randint(0, 9))
        digit2 = str(random.randint(0, 9))

        position1 = random.randint(0, len(s))
        position2 = random.randint(0, len(s))

        if position1 > position2:
            position1, position2 = position2, position1

        s = s[:position1] + digit1 + s[position1:]
        s = s[:position2 + 1] + digit2 + s[position2 + 1:]

        return s

    def generate_name(self):
        while True:
            name = ''
            person = Person('en')
            name += person.first_name()
            name += '-'
            name += person.last_name()
            name = self.add_random_digits(name)
            if len(name) < 10:
                continue
            available = self.contract.functions.available(name.lower()).call()
            if available is True:
                logger.info(f'Mint domen - {name.lower()}\n')
                return name.lower()

            else:
                time.sleep(1)
                continue

    @exception_handler('Mint domen')
    def register(self):
        check_register = self.contract.functions.discountedRegistrants(self.address_wallet).call()
        if check_register is True:
            logger.error(f'Account {self.address_wallet} already register domen\n')
            return False

        name = self.generate_name()
        name2 = name + '.base.eth'

        dick = {
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            **self.get_gas_price()
        }

        name_hash = self.namehash(name2)
        payload = to_hex(encode(['bytes32', 'string'], [name_hash, name2]))

        data = [
            Web3.to_bytes(hexstr=f'0xd5fa2b00{Web3.to_hex(name_hash)[2:]}000000000000000000000000{self.address_wallet[2:]}'),
            Web3.to_bytes(hexstr=f'0x77372213{payload[2:]}')
        ]

        request = (
                name,
                self.address_wallet,
                31557600,
                Web3.to_checksum_address('0xC6d566A56A1aFf6508b41f6c90ff131615583BCD'),
                data,
                True
        )

        txn = self.contract.functions.discountedRegister(
            request,
            Web3.to_bytes(hexstr='0xc1af3c32616941d3f6d85f4f01aafb556b5620e8868acac1ed2a816fb9d0676d'),
            Web3.to_bytes(hexstr='0x00')
        ).build_transaction(dick)

        self.send_transaction_and_wait(txn, f'Mint {name2} domen')

    @exception_handler('Mint domen')
    def register_paid(self):
        name = self.generate_name()
        name2 = name + '.base.eth'

        dick = {
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'value': Web3.to_wei(0.0001, 'ether'),
            **self.get_gas_price()
        }

        name_hash = self.namehash(name2)
        payload = to_hex(encode(['bytes32', 'string'], [name_hash, name2]))

        data = [
            Web3.to_bytes(hexstr=f'0xd5fa2b00{Web3.to_hex(name_hash)[2:]}000000000000000000000000{self.address_wallet[2:]}'),
            Web3.to_bytes(hexstr=f'0x77372213{payload[2:]}')
        ]

        txn = self.contract.functions.register(
            (
                name,
                self.address_wallet,
                31557600,
                Web3.to_checksum_address('0xC6d566A56A1aFf6508b41f6c90ff131615583BCD'),
                data,
                True
            )
        ).build_transaction(dick)

        self.send_transaction_and_wait(txn, f'Mint {name2} domen')
