import json

from solana.rpc.async_api import AsyncClient
from solana.publickey import PublicKey
import asyncio
from solana.rpc.api import Client
import datetime

async def get_balance(address: str):
    rpc_url = "https://api.mainnet-beta.solana.com"
    client = AsyncClient(rpc_url)

    try:
        public_key = PublicKey(address)
        response = await client.get_balance(public_key)

        if response.value:
            balance = response.value / 10 ** 9
            return float(balance)
        else:
            return 0.00
    except Exception as e:
        return 0.00
    finally:
        await client.close()


def get_transactions(address: str):
    rpc_url = "https://api.mainnet-beta.solana.com"
    client = Client(rpc_url)
    address = PublicKey(address)
    result = client.get_signatures_for_address(address)
    signatures = result.value
    if not signatures:
        return "No transactions found for this address."

    def serialize_transaction(transaction):
        return {
            "signature": transaction.signature,
            "slot": transaction.slot,
            "block_time": transaction.block_time,
            "confirmation_status": transaction.confirmation_status,
            "memo": transaction.memo,
            "err": transaction.err,
        }
    serialized_transactions = [serialize_transaction(tx) for tx in signatures]
    print(serialized_transactions)


print(get_transactions("FP5mLhaXw2NN7Xco3scX8i8QvK6muRXRrV1GfMTRjyGb"))
