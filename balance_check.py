
import asyncio
import json

from web3 import Web3
from web3.eth import AsyncEth


with open("data/rpc.json") as file:
    RPC = json.load(file)

def open_wallets():
    with open("config/wallets.txt", "r") as file:
        return [row.strip() for row in file]

async def check_balances(chain: str = "ethereum"):
    w3 = Web3(
            Web3.AsyncHTTPProvider(RPC[chain]["rpc"][0]),
            modules={"eth": (AsyncEth,)},
        )
    
    for wallet in open_wallets():
        print(f"{wallet} -> {w3.from_wei(await w3.eth.get_balance(wallet), 'ether')} ETH")

if __name__ == '__main__':
     asyncio.run(check_balances("zksync"))