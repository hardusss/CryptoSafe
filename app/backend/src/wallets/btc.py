import requests


def balance(address: str) -> float:
    """
    Get the balance of a Bitcoin address.

    :param address: The Bitcoin address to check.
    :return: The balance of the address in satoshi.
    """
    url = f"https://blockchain.info/q/addressbalance/{address}"
    response = requests.get(url)
    if response.status_code == 200:
        return float(response.text)
    else:
        print(f"Error {response.status_code}: {response.reason}")
        return 0.00
