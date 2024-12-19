import requests

req = requests.get("https://testnet.tonscan.org/address/kQDJ7ESl_zu0fbWkF0QHwmNjO3sM-CuS5dwX0NQb4HsMGTb7")
print(req.json())