import time
from settings import REF_CODE
from modules.wallet import Wallet
from loguru import logger
from modules.retry import exception_handler
import ua_generator
import requests

# with open('./address.txt', "r", encoding='utf-8') as f:
#     address = [row.strip() for row in f]


class BaseSummer(Wallet):
    def __init__(self, private_key, chain, number, proxy):
        super().__init__(private_key, chain, number, proxy)

    # def get_ref(self):
    #     url = f'https://basehunt.xyz/api/profile/state?userAddress={self.address_wallet}&gameId=2'
    #     data = self.get_api_call_data_get(url)
    #     return data['referralData']['referralCode']

    @exception_handler('Init account')
    def init_account(self):
        url = 'https://basehunt.xyz/api/profile/opt-in'

        json = {
            'gameId': 2,
            'referralId': REF_CODE,
            'userAddress': self.address_wallet
        }

        logger.info(json)

        data = self.get_api_call_data_post(url, json)
        if data['success'] is True:
            logger.success('Init success')
        else:
            logger.error(data)

    def check_spin_available(self):
        url = f'https://basehunt.xyz/api/spin-the-wheel?gameId=2&userAddress={self.address_wallet}'
        data = self.get_api_call_data_get(url)
        return data['spinData']['hasAvailableSpin']

    @exception_handler('Spin')
    def spin_the_roulette(self):
        res = self.check_spin_available()
        if res is True:
            url = 'https://basehunt.xyz/api/spin-the-wheel/execute'
            json = {
                'gameId': 2,
                'userAddress': self.address_wallet
            }
            data = self.get_api_call_data_post(url, json)
            logger.info(f'Successful spin, result: {data["spinData"]["lastSpinResult"]["points"]} {data["spinData"]["lastSpinResult"]["type"]}\n')
        else:
            logger.info("You've already made a spin today\n")
            return False

    @exception_handler('Claim point')
    def check_point(self):
        url = 'https://basehunt.xyz/api/challenges/complete'
        challenge_ids = {
            '6UuHdstl9MRFd4cgFf15kk': {
                'Butterfly': 250
            },
            '1iZiHPbqaIGW5F08bCit6J': {
                'URC x Base Launch': 150
            },
            '78AUXYw8UCyFUPE2zy9yMZ': {
                'ETH Breaking Through': 150
            },
            '1pjoNf5onjgsi7r9fWp3ob': {
                'Happy Birthday Toshi!': 250
            },
            '5e383RWcRtGAwGUorkGiYC': {
                'Celebrating the Ethereum ETF': 250
            },
            '2XaiAPDQ8WwG5CUWfMMYaU': {
                'Claim your BaseName.base.eth': 1000
            },
            '6VRBNN6qr2algysZeorek8': {
                'Team Liquid Onchain Summer': 500
            },
            '3WE9nylUC2bMHz9c6hxFnL': {
                'Toshi Vibe': 1000
            },
            '3ofLIMuInVt5sKkQOtLWp0': {
                'Stand with Crypto': 500
            },
            '359X8U2xzQmVIQRe7xSFk9': {
                'Endaoment X SWC Shield': 500
            },
            '1zbecUKJMKwyYoKOn2OV5n': {
                'Stand with Crypto Pizza': 500
            },
            '5Hyw2HMBfOBFDvCBkvdVmX': {
                'Stand With Crypto | Song A Day #5714': 500
            }, 
            'ocsChallenge_bd5208b5-ff1e-4f5b-8522-c4d4ebb795b7': {
                'STIX Launch Tournament Pass': 1000
            },
            'ocsChallenge_3809bf6d-a2d1-4e15-84e7-74beac310661': {
                'Base Turns One': 250
            },
            'ocsChallenge_d0778cee-ad0b-46b9-93d9-887b917b2a1f': {
                'Mister Miggles': 1000
            },
            'ocsChallenge_eba9e6f0-b7b6-4d18-8b99-a64aea045117': {
                'ETFEREUM': 150
            },
            'ocsChallenge_ee0cf23e-74a1-4bb3-badf-037a6bbf35e8': {
                'Ethereum ETF': 150
            },
            'ocsChallenge_65c17605-e085-4528-b4f1-76ce5f48da56': {
                'Post-ETH ETF Era': 150
            },
            'ocsChallenge_c1de2373-35ad-4f3c-ab18-4dfadf15754d': {
                'ETH cant be stopped': 150
            },
            'ocsChallenge_f161cd0e-7039-4e13-bfa8-1217fec5ccc6': {
                'Wish You Were Onchain': 1000
            },
            'ocsChallenge_1287a985-e4b1-4f30-b508-306c4d109832': {
                'EIC02 | Summer 24 Digital Edition': 500
            }
        }

        for challenge_id in challenge_ids.keys():

            json = {
                'challengeId': challenge_id,
                'gameId': 2,
                'userAddress': self.address_wallet
            }
            challenge_name, point = list(challenge_ids[challenge_id].items())[0]
            try:
                data = self.get_api_call_data_post(url, json)
                if data['message'] == 'challenge-claimed':
                    logger.info(f'Challenge {challenge_name} already claimed {point} point')
                elif data['message'] == 'challenge-completed':
                    logger.info(f'Challenge {challenge_name} successful claimed {point} point')
                else:
                    logger.info(f'Challenge {challenge_name} not complete')

            except:
                logger.error(f'Claim points for NFT id {challenge_id} is over')

            time.sleep(1)

    @exception_handler('Claim badge')
    def claim_badge(self):
        url = 'https://basehunt.xyz/api/badges/claim'
        for i in range(1, 11):
            json = {
                'badgeId': str(i),
                'gameId': 2,
                'userAddress': self.address_wallet
            }

            data = self.get_api_call_data_post(url, json)
            logger.info(data)
            time.sleep(1)

    @staticmethod
    def generate_wallet_table(wallet_data, filename="./data/wallet_stat.txt"):
        existing_data = {}

        try:
            with open(filename, 'r') as file:
                lines = file.readlines()[2:]
                for line in lines:
                    parts = line.strip().split()
                    wallet = parts[0]
                    badges = int(parts[1])
                    level = int(parts[2])
                    challenges_completed = int(parts[3])
                    num_referrals = int(parts[4])
                    current_score = int(parts[5])

                    existing_data[wallet] = {
                        "badges": badges,
                        "level": level,
                        "ChallengesCompleted": challenges_completed,
                        "numReferrals": num_referrals,
                        "currentScore": current_score,
                    }
        except FileNotFoundError:
            pass

        for wallet, data in wallet_data.items():
            existing_data[wallet] = data

        with open(filename, 'w') as file:
            file.write(f"{'Wallet':<45} {'Badges':^10} {'Level':^7} {'ChallengesCompleted':^20} {'NumReferrals':^15} {'CurrentScore':^15}\n")
            file.write('-' * 120 + '\n')

            for wallet, data in existing_data.items():
                badges = data.get("badges", 0)
                level = data.get("level", 0)
                challenges_completed = data.get("ChallengesCompleted", 0)
                num_referrals = data.get("numReferrals", 0)
                current_score = data.get("currentScore", 0)

                file.write(f"{wallet:<45} {badges:^10} {level:^7} {challenges_completed:^20} {num_referrals:^15} {current_score:^15}\n")

    def check_stat(self):
        url = f'https://basehunt.xyz/api/profile/state?userAddress={self.address_wallet}&gameId=2'
        data = self.get_api_call_data_get(url)
        badge = len(data['badges'])
        level = data['levelData']['currentLevel']['level']
        challenges_completed = data['numChallengesCompleted']
        num_referal = data['referralData']['numReferrals']
        score = data['scoreData']['currentScore']

        wallet_data = {
            self.address_wallet: {
                "badges": badge, "level": level, "ChallengesCompleted": challenges_completed,
                "numReferrals": num_referal, "currentScore": score
            }
        }

        self.generate_wallet_table(wallet_data)

