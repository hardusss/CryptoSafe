import requests


def balance(address) -> float:

    url = f'https://api.trongrid.io/v1/accounts/{address}'

    response = requests.get(url)
    data = response.json()

    if 'data' in data and len(data['data']) > 0:
        balance = data['data'][0]['balance'] / 10**6
        return float(balance)
    else:
        return 0.00
