from modules.chain import *

# General Settings (ОСНОВНЫЕ НАСТРОЙКИ)

EXCEL_PASSWORD =  False                # Если ставите пароль на Excel с приватниками || True/ False
SHUFFLE_WALLETS = True                 # Перемешка кошельков                         || True/ False

TG_BOT_SEND = False                    # Включить уведомления в тг или нет           || True/ False
TG_TOKEN = ''                          # API токен тг-бота - создать его можно здесь - https://t.me/BotFather
TG_ID = 0                              # id твоего телеграмма можно узнать тут       - https://t.me/getmyid_bot

CHAIN_RPC = {
    Ethereum: 'https://rpc.ankr.com/eth',
    Base    : 'https://rpc.zerion.io/v1/base',
}

MAX_GAS_ETH = 20                       # max gas в gwei (смотреть здесь : https://etherscan.io/gastracker)
MAX_GAS_BASE = 0.2                     # max gas в base (смотреть здесь : https://cointool.app/gasPrice/base)
SLIPPAGE = 1

RETRY = 2                              # Количество попыток при ошибках / фейлах
TIME_DELAY = [30, 60]                  # Задержка после ТРАНЗАКЦИЙ     [min, max]
TIME_ACCOUNT_DELAY = [50, 100]         # Задержка между АККАУНТАМИ     [min, max]
TIME_DELAY_ERROR = [10, 20]            # Задержка при ошибках / фейлах [min, max]

REF_CODE = '5cecb41a-969e-4eb7-83b8-b0c1609436a8'    # Ref code onchain summer (вставляйте рефку своего мейна)

# Sold Token (ПРОДАЖА ТОКЕНОВ)

odos_token = [
    '0xb8d98a102b0079b69ffbc760c8d857a31653e56e' # $toby
]

# Custom routes (КАСТОМНЫЕ МОДУЛИ)

ROUTES = [
    ['mint_toshi_vibe'],
    ['mint_mister_miggles'],
    ['mint_stand_with_crypto'],
    ['mint_team_liquid'],
    ['mint_wywo'],
]
'''
    Список доступных модулей
        'mint_python_zorb_opensea'     # Наша для FREE NFT прогрева
        'vote_rubyscore'               # FREE голосование на RubyScore в BASE
        'sold_token_odos'              # Продажа всего баланса, выбранного токена(щиктоина например)

        # ONCHAIN SUMMER QUESTS
     
        'mint_eurc'                    # EURC x Base Launch                  (0.0001 ETH - 150 points)
        'mint_celebrating_etf'         # Celebrating the Ethereum ETF        (0.0001 ETH - 250 points)
        'mint_happy_birthday_toshi'    # Happy Birthday Toshi                (0.0001 ETH - 250 points)
        'mint_eth_breaking_through'    # ETH BREAKING THROUGH                (0.0001 ETH - 150 points)
        'mint_eth_cant_stopped'        # ETH can't be stopped                (0.0001 ETH - 150 points)
        'mint_the_world_after'         # the world after ETH ETF approval    (0.0001 ETH - 150 points)
        'mint_ethereum_etf'            # Ethereum ETF                        (0.0001 ETH - 150 points)
        'mint_ethereum'                # ETFEREUM                            (0.0001 ETH - 150 points)
        'mint_coinbase_wallet'         # Introducing: Coinbase Wallet        (0.0001 ETH - 250 points)
        'mint_team_liquid'             # Team Liquid Onchain Summer          (Free - 500 points)
        'mint_mister_miggles'          # Mister Miggles                      (0.0002 ETH - 1000 points)
        'mint_stix'                    # STIX Launch Tournament Pass         (Free - 1000 points)
        'mint_smart_wallet'            # Mint Introducing Smart Wallet       (Free - END)
        'mint_wywo'                    # Wish You Were Onchain               (Free - 1000 points)
        'mint_toshi_vibe'              # Toshi Vibe                          (0.0001 ETH - 1000 points)
        'mint_song_a_day'              # Stand With Crypto | Song A Day #57  (0.0001 ETH - 500 points)
        'mint_crypto_pizza'            # Stand with Crypto Pizza             (0.0001 ETH - 500 points)
        'mint_endaoment_shield'        # Endaoment X SWC Shield              (0.0001 ETH - 500 points)
        'mint_stand_with_crypto'       # Stand with Crypto                   (0.0001 ETH - 500 points)
        
        'init_account_on_base_summer'  # Зарегать акки по своей рефке
        'spin_roulette'                # Крутим рулетку на всех акках        (Нужен 1 уровень - 250+ points)
        'claim_point'                  # Собираем поинты с заданий
        'claim_badge'                  # Клейм доступных бейджей
        'register_domain'              # Нужен 3 уровень (5000 points) - сначала набираем его, а потом клеймим домен (Free - 1000 points)
'''

ROUTES_SHUFFLE = True              # Перемешка модулей
TIME_DELAY_ROUTES = [30, 50]       # Задержка между МОДУЛЯМИ     [min, max]
