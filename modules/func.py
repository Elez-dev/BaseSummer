import io
from msoffcrypto.exceptions import DecryptionError, InvalidKeyError
from loguru import logger
from settings import EXCEL_PASSWORD, SHUFFLE_WALLETS
import random
from tqdm import tqdm
import time
import msoffcrypto
import pandas as pd


def shuffle(wallets_list):
    if SHUFFLE_WALLETS is True:
        numbered_wallets = list(enumerate(wallets_list, start=1))
        random.shuffle(numbered_wallets)
    elif SHUFFLE_WALLETS is False:
        numbered_wallets = list(enumerate(wallets_list, start=1))
    else:
        raise ValueError("\nНеверное значение переменной 'shuffle_wallets'. Ожидается 'True' or 'False'.")
    return numbered_wallets


def sleeping(sleep_from: int, sleep_to: int):
    delay = random.randint(sleep_from, sleep_to)
    time.sleep(1)
    with tqdm(
            total=delay,
            desc="💤 Sleep",
            bar_format="{desc}: |{bar:20}| {percentage:.0f}% | {n_fmt}/{total_fmt}",
            colour="green"
    ) as pbar:
        for _ in range(delay):
            time.sleep(1)
            pbar.update(1)
    time.sleep(1)
    print()


def get_accounts_data():

    decrypted_data = io.BytesIO()

    try:
        with open('./data/accounts_data.xlsx', 'rb') as file:
            if EXCEL_PASSWORD:
                time.sleep(1)
                password = input('Enter the password: ')  # Request the password

                office_file = msoffcrypto.OfficeFile(file)

                try:
                    office_file.load_key(password=password)
                    office_file.decrypt(decrypted_data)
                except msoffcrypto.exceptions.InvalidKeyError:
                    logger.error('\n⚠️ Invalid key to decrypt Excel file! ⚠️\n')
                    raise InvalidKeyError('Invalid key')
                except msoffcrypto.exceptions.DecryptionError:
                    logger.error('\n⚠️ Incorrect password to decrypt Excel file! ⚠️\n')
                    raise DecryptionError('Incorrect password')

                wb = pd.read_excel(decrypted_data)
            else:
                wb = pd.read_excel(file)
    except FileNotFoundError:
        logger.error(f'\n⚠️ File not found ⚠️\n')
        raise
    except Exception as error:
        logger.error(f'\n⚠️ Error reading Excel file: {error} ⚠️\n')
        raise

    accounts_data = {}
    for index, row in wb.iterrows():
        proxy = row['PROXY']
        private_key_evm = row['PRIVATE KEY EVM']
        accounts_data[int(index) + 1] = {
            "proxy": proxy,
            'private_key_evm': private_key_evm
        }

    prx, pk = [], []
    for account in accounts_data.values():
        if isinstance(account['private_key_evm'], str):
            pk.append(account['private_key_evm'])
        prx.append(account['proxy'] if isinstance(account['proxy'], str) else None)

    return list(zip(pk, prx))
