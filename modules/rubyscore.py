from modules.wallet import Wallet
from loguru import logger
from modules.retry import exception_handler
from web3 import Web3


class RubyScore(Wallet):
    def __init__(self, private_key, chain, number, proxy):
        super().__init__(private_key, chain, number, proxy)

    @exception_handler('Vote on rubyscore')
    def vote(self):
        logger.info(f'Vote on rubyscore')
        tx = {
            'chainId': self.web3.eth.chain_id,
            'data': '0x632a9a52',
            'from': self.address_wallet,
            'to': Web3.to_checksum_address('0xe10add2ad591a7ac3ca46788a06290de017b9fb4'),
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'gas': 150_000,
            **self.get_gas_price()
        }

        gas = self.web3.eth.estimate_gas(tx)
        tx.update({'gas': gas})

        self.send_transaction_and_wait(tx, 'Vote on rubyscore')
