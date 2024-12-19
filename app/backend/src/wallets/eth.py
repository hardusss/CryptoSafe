from web3 import Web3
from dotenv import load_dotenv
from os import getenv


load_dotenv()
infura_url = f'https://mainnet.infura.io/v3/{getenv("API_KEY")}'
web3 = Web3(Web3.HTTPProvider(infura_url))


def balance(address) -> float:
    """
    Get the balance of a given Ethereum address in Ether.

    Args:
        address (str): Ethereum address to fetch balance for.

    Returns:
        float: The balance of the given Ethereum address in Ether.
    """
    # Convert balance from Wei to Ether
    try:
        balance_wei = web3.eth.get_balance(address)
        return float(web3.from_wei(balance_wei, "ether"))
    except:
        return 0.00


