from sys import stdout
from modules import *
from modules.custom_route import CustomRouter
from settings import ROUTES, TIME_ACCOUNT_DELAY, ROUTES_SHUFFLE, CHAIN_RPC, odos_token, TIME_DELAY
import time
import json

logger.remove()
logger.add("./data/log.txt")
logger.add(stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <7}</level> | <cyan>{message}</cyan>")
web3_eth = Web3(Web3.HTTPProvider(CHAIN_RPC['Ethereum'], request_kwargs={'timeout': 1}))


class Worker:
    def __init__(self, action):
        self.action = action

    @staticmethod
    def generate_route():
        dick = {}
        for number, key in keys_list:

            address = web3_eth.eth.account.from_key(key[0]).address
            new_routes = []

            if ROUTES_SHUFFLE is True:
                random.shuffle(ROUTES)

            for subarray in ROUTES:
                if isinstance(subarray, list):
                    new_routes.append(random.choice(subarray))
                elif isinstance(subarray, str):
                    new_routes.append(subarray)
                else:
                    new_routes.append(None)

            dick[address] = {
                'index': 0,
                'route': new_routes
            }

        with open('./data/router.json', 'w') as f:
            json.dump(dick, f)

        logger.success('Successfully generated route\n')

    @staticmethod
    def mint_with_comment(key, str_number, proxy, nft_number):
        nft = MintNFT(key, Base, str_number, proxy)
        return nft.mint_base_summer_nft(nft_number - 4)

    def work(self):
        i = 0
        for number, acc in keys_list:
            key, proxy = acc
            str_number = f'{number} / {all_wallets}'
            i += 1
            address = web3_eth.eth.account.from_key(key).address
            logger.info(f'Account #{i} || {address}\n')

            if self.action == 1:
                nft = MintNFT(key, Base, str_number, proxy)
                nft.mint_python_zorb_base_opensea()

            if self.action == 2:
                vote = RubyScore(key, Base, str_number, proxy)
                vote.vote()

            if self.action == 3:
                od = OdosSwap(key, Base, str_number, proxy)
                for token in odos_token:
                    res = od.sold_token(token)
                    if res is False:
                        continue
                    sleeping(TIME_DELAY[0], TIME_DELAY[1])

            if self.action in range(4, 35):
                res = self.mint_with_comment(key, str_number, proxy, self.action)
                if res is False:
                    continue

            if self.action == 35:
                nft = MintNFT(key, Base, str_number, proxy)
                nft.mint_web_app()

            if self.action == 36:
                nft = MintNFT(key, Base, str_number, proxy)
                nft.mint_buildathon()

            if self.action == 37:
                nft = MintNFT(key, Base, str_number, proxy)
                nft.mint_mister_migless()

            if self.action == 38:
                nft = MintNFT(key, Base, str_number, proxy)
                nft.mint_smart_wallet()

            if self.action == 39:
                nft = MintNFT(key, Base, str_number, proxy)
                nft.mint_liquid()

            if self.action == 40:
                nft = MintNFT(key, Base, str_number, proxy)
                res = nft.mint_juice()
                if res is False:
                    continue

            if self.action == 41:
                nft = MintNFT(key, Base, str_number, proxy)
                res = nft.mint_forbes()
                if res is False:
                    continue

            if self.action == 42:
                nft = MintNFT(key, Base, str_number, proxy)
                res = nft.mint_truworld_onchain()
                if res is False:
                    continue

            if self.action == 43:
                base = BaseSummer(key, Base, str_number, proxy)
                base.init_account()

            if self.action == 44:
                base = BaseSummer(key, Base, str_number, proxy)
                res = base.spin_the_roulette()
                if res is False:
                    continue

            if self.action == 45:
                base = BaseSummer(key, Base, str_number, proxy)
                base.claim_badge()

            if self.action == 46:
                base = BaseSummer(key, Base, str_number, proxy)
                base.check_point()

            if self.action == 47:
                base = Domen(key, Base, str_number, proxy)
                res = base.register()
                if res is False:
                    continue

            if self.action == 48:
                base = Domen(key, Base, str_number, proxy)
                base.register_paid()

            if self.action == 49:
                base = BaseSummer(key, Base, str_number, proxy)
                base.check_stat()
                time.sleep(1)
                continue

            if self.action == 51:
                router = CustomRouter(key, str_number, proxy)
                res = router.run()
                if res is False:
                    continue

            logger.success(f'Account completed, sleep and move on to the next one\n')
            sleeping(*TIME_ACCOUNT_DELAY)


if __name__ == '__main__':
    list1 = get_accounts_data()
    all_wallets = len(list1)
    logger.info(f'Number of wallets: {all_wallets}\n')
    keys_list = shuffle(list1)

    while True:
        while True:
            logger.info('''
1  - Mint Python Zorb OpenSea                 (старый модуль просто для прогрева акков)
2  - Vote on RubyScore                        (старый модуль просто для прогрева акков)
3  - Sold token Odos                          (можно продать какой-нибудь щиткоин)

4  - Mint EURC x Base Launch                  (0.0001 ETH - 150 points)
5  - Mint celebrating the Ethereum ETF        (0.0001 ETH - 250 points)
6  - Mint Happy Birthday Toshi                (0.0001 ETH - 250 points)
7  - Mint ETH BREAKING THROUGH                (0.0001 ETH - 150 points)
8  - Mint ETH can't be stopped                (0.0001 ETH - 150 points)
9  - Mint the world after ETH ETF approval    (0.0001 ETH - 150 points)
10 - Mint Ethereum ETF                        (0.0001 ETH - 150 points)
11 - Mint ETFEREUM                            (0.0001 ETH - 150 points)
12 - Mint Toshi Vibe                          (0.0001 ETH - 1000 points)
13 - Stand With Crypto | Song A Day #5714     (0.0001 ETH - 500 points)
14 - Stand with Crypto Pizza                  (0.0001 ETH - 500 points)
15 - Endaoment X SWC Shield                   (0.0001 ETH - 500 points)
16 - Stand with Crypto                        (0.0001 ETH - 500 points)
17 - strut 001                                (0.0001 ETH - 500 points)
18 - Crypto will bloom                        (0.0001 ETH - 500 points)
19 - What if we added a S                     (0.0001 ETH - 1000 points)
20 - Crypto Vibe(CV)                          (0.0001 ETH - 500 points)
21 - The Creative Shield                      (0.0001 ETH - 500 points)
22 - Toshi x SWC 3                            (0.0001 ETH - 500 points)
23 - duality in motion                        (0.0001 ETH - 500 points)
24 - en garde                                 (0.0001 ETH - 500 points)
26 - Mint the vision                          (0.0001 ETH - 1000 points)
27 - Stand With Crypto Shield Rune            (0.0001 ETH - 500 points)
28 - Shielding the wonder                     (0.0001 ETH - 500 points)
29 - Earth Stands with Crypto                 (0.0001 ETH - 500 points)
30 - ⌐◨-◨ Stand With Crypto                   (0.0001 ETH - 500 points)
31 - we stand, we build                       (0.0001 ETH - 500 points)
32 - Let The Shield Shine                     (0.0001 ETH - 500 points)
33 - All for One                              (0.0001 ETH - 500 points)
34 - Even Sam Stands with Crypto              (0.0001 ETH - 500 points)
35 - Mint Introducing: Coinbase Wallet        (0.0001 ETH - 250 points)
36 - Mint Buildathon                          (0.0002 ETH - нужна ТОЛЬКО для бейджа Builder)
37 - Mint Mister Miggles                      (0.0002 ETH - 1000 points)
38 - Mint Introducing Smart Wallet            (Free - END)
39 - Mint Team Liquid Onchain Summer          (Free - 500 points)
40 - Mint Juicy Adventure Onch                (Free - 1000 points)
41 - Mint Forbes Web3 INSPIRE                 (Free - 1000 points)
42 - Mint Truworld Onchain Mobile Pass        (Free - 500 points)

43 - Init account on Base Summer              (зарегать акки по своей рефке)
44 - Spin roulette on Base Summer             (рулетка ТОЛЬКО после первого уровня: 250+ points)
45 - Claim badge for Base Summer              (клейм доступных бейджей)
46 - Claim point for NFT Base Summer          (собирает награды с заданий)
47 - Mint free BASE domain                    (нужен 3 уровень - сначала набираем его, а потом клеймим домен)
48 - Mint paid Base domain                    (0.0001 ETH) 
49 - Check Stat

50 - Generate Сustom routes                   (сначала запускаем этот модуль, потом модуль 51)
51 - Rus Сustom routes
''')

            time.sleep(0.1)
            act = int(input('Choose an action: '))

            if act == 50:
                Worker.generate_route()
                continue

            if act in range(1, 52):
                break

        worker = Worker(act)
        worker.work()
