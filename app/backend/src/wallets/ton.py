import requests


def balance(address, *, is_testnet: bool = False) -> float:
    """
    Get the TON balance of an address.
    :param address: The address in ton blockchain to get the balance
    :param is_testnet: bool, optional, default False. If True, use the testnet TON network.
    :return: float: TON balance
    """
    url = f"https://{'testnet.' if is_testnet else ''}toncenter.com/api/v2/getAddressInformation"

    # Params query
    params = {
        "address": address
    }

    # Send request
    response = requests.get(url, params=params)

    if response.status_code == 200:
        balance_info = response.json()
        print(balance_info)
        balance_nano = balance_info["result"]["balance"]
        balance_ton = float(balance_nano) / 1_000_000_000
        return balance_ton
    else:
        return 0.00


# TEST
if __name__ == '__main__':
    print(balance("0QAgCe0xzXDh4K83UhYUvr5Up8AlA9pn0b_BR-U1TL2nv10e", is_testnet=True))
