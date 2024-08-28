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
TIME_ACCOUNT_DELAY = [200, 300]          # Задержка между АККАУНТАМИ     [min, max]
TIME_DELAY_ERROR = [10, 20]            # Задержка при ошибках / фейлах [min, max]

REF_CODE = '5cecb41a-969e-4eb7-83b8-b0c1609436a8'          # Ref code onchain summer (вставляйте рефку своего мейна)
                                                           # в скобочках рефка -> wallet.coinbase.com/summer/share/summerpass?referral_id=(5cecb41a-969e-4eb7-83b8-b0c1609436a8)&summerpass_id=
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
    ['claim_badge'],
]
'''
    Список доступных модулей
        'mint_python_zorb_opensea'     # Наша для FREE NFT прогрева
        'vote_rubyscore'               # FREE голосование на RubyScore в BASE
        'sold_token_odos'              # Продажа всего баланса, выбранного токена(щиктоина например)

        # ONCHAIN SUMMER QUESTS
     
        'mint_eurc'                    # EURC x Base Launch                  (0.0001 ETH - 150 points)
        'mint_eth_breaking_through'    # ETH BREAKING THROUGH                (0.0001 ETH - 150 points)
        'mint_eth_cant_stopped'        # ETH can't be stopped                (0.0001 ETH - 150 points)
        'mint_the_world_after'         # the world after ETH ETF approval    (0.0001 ETH - 150 points)
        'mint_ethereum_etf'            # Ethereum ETF                        (0.0001 ETH - 150 points)
        'mint_ethereum'                # ETFEREUM                            (0.0001 ETH - 150 points)
        'mint_celebrating_etf'         # Celebrating the Ethereum ETF        (0.0001 ETH - 250 points)
        'mint_happy_birthday_toshi'    # Happy Birthday Toshi                (0.0001 ETH - 250 points)
        'mint_coinbase_wallet'         # Introducing: Coinbase Wallet        (0.0001 ETH - 250 points)
        'mint_smart_wallet'            # Mint Introducing Smart Wallet       (Free - поинты не получить, но нфт можно минтить)
        'mint_team_liquid'             # Team Liquid Onchain Summer          (Free - 500 points)    
        'mint_mister_miggles'          # Mister Miggles                      (0.0002 ETH - 1000 points)
        'mint_toshi_vibe'              # Toshi Vibe                          (0.0001 ETH - 1000 points)
        'mint_song_a_day'              # Stand With Crypto | Song A Day #57  (0.0001 ETH - 500 points)
        'mint_crypto_pizza'            # Stand with Crypto Pizza             (0.0001 ETH - 500 points)
        'mint_endaoment_shield'        # Endaoment X SWC Shield              (0.0001 ETH - 500 points)
        'mint_stand_with_crypto'       # Stand with Crypto                   (0.0001 ETH - 500 points)
        'mint_strut001'                # strut 001                           (0.0001 ETH - 500 points)
        'mint_what_if_we_added'        # What if we added a S                (0.0001 ETH - 1000 points)
        'mint_crypto_vibe'             # Crypto Vibe(CV)                     (0.0001 ETH - 500 points)
        'mint_creative_shield'         # The Creative Shield                 (0.0001 ETH - 500 points)
        'mint_toshi3'                  # Toshi x SWC 3                       (0.0001 ETH - 500 points)
        'mint_duality_in_motion'       # duality in motion                   (0.0001 ETH - 500 points)
        'mint_en_garde'                # en garde                            (0.0001 ETH - 500 points)
        'mint_juicy_adventure'         # Juicy Adventure Onch                (Free - 1000 points)
        'mint_live_and_let_live'        # Live and Let Live!                 (0.0005 ETH - 5000 points)
        'mint_the_vision'               # Mint the vision                    (0.0001 ETH - 1000 points)
        'mint_shield_rune'              # Stand With Crypto Shield Rune      (0.0001 ETH - 500 points)
        'mint_shielding_the_wonder'     # Shielding the wonder               (0.0001 ETH - 500 points)
        'mint_earth_stands_with_crypto' # Earth Stands with Crypto           (0.0001 ETH - 500 points)
        'mint_with_crypto'              # ⌐◨-◨ Stand With Crypto             (0.0001 ETH - 500 points)
        'mint_we_build'                 # we stand, we build                 (0.0001 ETH - 500 points)
        'mint_the_shield_shine'         # Let The Shield Shine               (0.0001 ETH - 500 points)
        'mint_all_for_one'              # All for One                        (0.0001 ETH - 500 points)
        'mint_even_sam'                 # Even Sam Stands with Crypto        (0.0001 ETH - 500 points)
        'mint_forbes'                   # Forbes Web3 INSPIRE                (Free - 1000 points)
        
        'init_account_on_base_summer'  # Зарегать акки по своей рефке
        'spin_roulette'                # Крутим рулетку на всех акках        (Нужен 1 уровень - 250+ points)
        'claim_point'                  # Собираем поинты с заданий
        'claim_badge'                  # Клейм доступных бейджей
        'register_domain'              # Нужен 3 уровень (5000 points) - сначала набираем его, а потом клеймим домен (Free - 1000 points)
'''

ROUTES_SHUFFLE = True              # Перемешка модулей
TIME_DELAY_ROUTES = [30, 50]       # Задержка между МОДУЛЯМИ     [min, max]
