from web3.exceptions import TransactionNotFound
from loguru import logger
from settings import RETRY, TIME_DELAY_ERROR
from modules.func import sleeping
from web3 import Web3
from settings import MAX_GAS_ETH, CHAIN_RPC, MAX_GAS_BASE
import time

web3_eth = Web3(Web3.HTTPProvider(CHAIN_RPC['Ethereum'], request_kwargs={'timeout': 60}))
web3_base = Web3(Web3.HTTPProvider(CHAIN_RPC['Base'], request_kwargs={'timeout': 60}))


def check_gas_eth():
    while True:
        try:
            res = int(Web3.from_wei(web3_eth.eth.gas_price, 'gwei'))
            logger.info(f'GAS ETH - {res} gwei')
            if res <= MAX_GAS_ETH:
                break
            else:
                time.sleep(60)
                continue
        except Exception as error:
            logger.error(error)
            time.sleep(30)
            continue


def check_gas_base():
    while True:
        try:
            res = float(Web3.from_wei(web3_base.eth.gas_price, 'gwei'))
            logger.info(f'GAS BASE - {res} gwei\n')
            if res <= MAX_GAS_BASE:
                break
            else:
                time.sleep(60)
                continue
        except Exception as error:
            logger.error(error)
            time.sleep(30)
            continue


def exception_handler(label=''):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            for _ in range(RETRY):
                try:
                    check_gas_eth()
                    check_gas_base()
                    return func(self, *args, **kwargs)

                except TransactionNotFound:
                    logger.error('Транзакция не смайнилась за долгий промежуток времени, пытаюсь еще раз\n')
                    self.send_message_error(self.number, label, self.address_wallet,
                                            'Транзакция не смайнилась за долгий промежуток времени, пытаюсь еще раз')
                    sleeping(TIME_DELAY_ERROR[0], TIME_DELAY_ERROR[1])

                except ConnectionError:
                    logger.error('Ошибка подключения к интернету или проблемы с РПЦ\n')
                    self.send_message_error(self.number, label, self.address_wallet,
                                            'Ошибка подключения к интернету или проблемы с РПЦ')
                    sleeping(TIME_DELAY_ERROR[0], TIME_DELAY_ERROR[1])

                except Exception as error:
                    if isinstance(error.args[0], dict):
                        if 'insufficien' in error.args[0]['message'] or 'required exceeds allowance' in error.args[0]['message']:
                            logger.error('Ошибка, скорее всего нехватает комсы\n')
                            self.send_message_error(self.number, label, self.address_wallet,
                                                    'Ошибка, скорее всего нехватает комсы')
                            return 'balance'
                        else:
                            logger.error(error)
                            self.send_message_error(self.number, label, self.address_wallet, error)
                            sleeping(TIME_DELAY_ERROR[0], TIME_DELAY_ERROR[1])
                    else:
                        logger.error(error)
                        self.send_message_error(self.number, label, self.address_wallet, error)
                        sleeping(TIME_DELAY_ERROR[0], TIME_DELAY_ERROR[1])
            else:
                return False
        return wrapper
    return decorator
