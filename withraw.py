import json
import random
import time
import okx.Funding as Funding

with open("config/okx.json", "r") as f: 
    okx = json.load(f)
    
    API_KEY = okx["api_key"]
    SECRET_KEY = okx["secret"]
    PASSPHRASE =okx["passphrase"]

AMOUNT = 0.005

FEE = "0.00015"

CHAIN = "ETH-zkSync Era"

def open_wallets():
    with open("config/wallets.txt", "r") as file:
        return [row.strip() for row in file]
    
def print_currencies():
    fundingAPI = Funding.FundingAPI(API_KEY, SECRET_KEY, PASSPHRASE, False, "0")

    resp = fundingAPI.get_currencies(ccy="ETH")  
    for ccy in resp["data"]:
        print(f"Currency: {ccy['ccy']}, chain: {ccy['chain']}, min fee: {ccy['minFee']}")
        print("--------------------------")


def withdraw():
    fundingAPI = Funding.FundingAPI(API_KEY, SECRET_KEY, PASSPHRASE, False, "0")

    for wallet in open_wallets():
        amount_to_send = round(AMOUNT * random.uniform(0.95, 1.0), 5)
        # amount_to_send = AMOUNT
        print(f"sending {amount_to_send} to {wallet}")
        resp = fundingAPI.withdrawal(ccy="ETH", amt=amount_to_send, dest=4, toAddr=wallet, fee=FEE, chain=CHAIN)
        print(f"Response: {resp}")
        print("Sleep for 1 sec...")
        time.sleep(1)

if __name__ == "__main__":
    print_currencies()
    # withdraw()