from modules import *
from settings import *
import json
from web3 import Web3
from loguru import logger

web3_eth = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth', request_kwargs={'timeout': 60}))


class CustomRouter:
    def __init__(self, private_key, number, proxy):
        self.number = number
        self.private_key = private_key
        self.proxy = proxy

    def mint_python_zorb_opensea(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_python_zorb_base_opensea()

    def vote_rubyscore(self):
        vote = RubyScore(self.private_key, Base, self.number, self.proxy)
        vote.vote()

    def sold_token_odos(self):
        od = OdosSwap(self.private_key, Base, self.number, self.proxy)
        for token in odos_token:
            res = od.sold_token(token)
            if res is False:
                continue
            sleeping(TIME_DELAY[0], TIME_DELAY[1])

    def mint_eurc(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(0)

    def mint_celebrating_etf(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(1)

    def mint_happy_birthday_toshi(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(2)

    def mint_eth_breaking_through(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(3)

    def mint_eth_cant_stopped(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(4)

    def mint_the_world_after(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(5)

    def mint_ethereum_etf(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(6)

    def mint_ethereum(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(7)

    def mint_song_a_day(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(9)

    def mint_crypto_pizza(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(10)

    def mint_endaoment_shield(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(11)

    def mint_stand_with_crypto(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(12)

    def mint_coinbase_wallet(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_web_app()

    def mint_strut001(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(13)

    def mint_crypto_will_bloom(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(14)

    def mint_what_if_we_added(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(15)

    def mint_crypto_vibe(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(16)

    def mint_creative_shield(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(17)

    def mint_toshi3(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(18)

    def mint_duality_in_motion(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(19)

    def mint_en_garde(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(20)

    def mint_live_and_let_live(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(21)

    def mint_the_vision(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(22)

    def mint_shield_rune(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(23)

    def mint_shielding_the_wonder(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(24)

    def mint_earth_stands_with_crypto(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(25)

    def mint_with_crypto(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(26)

    def mint_we_build(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(27)

    def mint_the_shield_shine(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(28)

    def mint_all_for_one(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(29)

    def mint_even_sam(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(30)

    def mint_forbes(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_forbes()

    def mint_truworld(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_truworld_onchain()

    def mint_juicy_adventure(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_juice()

    def mint_team_liquid(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_liquid()

    def mint_mister_miggles(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_mister_migless()

    def mint_smart_wallet(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_smart_wallet()

    def init_account_on_base_summer(self):
        base = BaseSummer(self.private_key, Base, self.number, self.proxy)
        base.init_account()

    def spin_roulette(self):
        base = BaseSummer(self.private_key, Base, self.number, self.proxy)
        base.spin_the_roulette()

    def claim_point(self):
        base = BaseSummer(self.private_key, Base, self.number, self.proxy)
        base.check_point()

    def claim_badge(self):
        base = BaseSummer(self.private_key, Base, self.number, self.proxy)
        base.claim_badge()

    def register_domain(self):
        base = Domen(self.private_key, Base, self.number, self.proxy)
        base.register()

    def mint_toshi_vibe(self):
        nft = MintNFT(self.private_key, Base, self.number, self.proxy)
        nft.mint_base_summer_nft(8)

    def save_progress(self, data, index):
        address = web3_eth.eth.account.from_key(self.private_key).address
        data[address]['index'] = index
        with open('./data/router.json', 'w') as f:
            json.dump(data, f)

    def run(self):
        address = web3_eth.eth.account.from_key(self.private_key).address
        data = json.load(open('./data/router.json'))
        try:
            route = data[address]['route']
            index = data[address]['index']
        except:
            return False

        flag = False

        while index < len(route):
            method_name = route[index]
            if method_name is None:
                index += 1
                continue
            if hasattr(self, method_name):
                logger.info(f'Module - {method_name}\n')
                if hasattr(self, method_name):
                    method = getattr(self, method_name)
                    res = method()
                    if res is False:
                        continue
                    flag = True
                    logger.success(f'Module completed, sleep and move on to the next one\n')

                    index += 1
                    self.save_progress(data, index)

                    sleeping(TIME_DELAY_ROUTES[0], TIME_DELAY_ROUTES[1])
            else:
                logger.error(f'Module - {method_name} not found\n')

        else:
            return flag
