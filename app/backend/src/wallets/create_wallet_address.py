from cryptography.fernet import Fernet
from bitcoinlib.wallets import Wallet, WalletError
import uuid
from tronpy.keys import PrivateKey
from tonsdk.contract.wallet import Wallets, WalletVersionEnum
from solana.keypair import Keypair
import base64
from eth_account import Account


class WalletAddressGenerator:
    """
    This class generates wallet addresses and private keys for different blockchains such as Bitcoin (BTC), Tron (TRX),
    The Open Network (TON), Solana (SOL), Ethereum (ETH), and Binance Smart Chain (BNB).

    It provides methods to generate unique wallet addresses and private keys for each blockchain. In case of an error
    during wallet generation, an error message will be returned instead.
    """

    def __init__(self, encryption_key: bytes = None):
        """
        Initializes the WalletAddressGenerator with an optional encryption key.

        If no encryption key is provided, a new one is generated. The encryption key is used to encrypt and decrypt
        private keys for secure storage.

        :param encryption_key: A 32-byte encryption key for encrypting private keys. Defaults to None.
        """
        if encryption_key is None:
            encryption_key = Fernet.generate_key()
        self.cipher = Fernet(encryption_key)

    def encrypt_private_key(self, private_key: str) -> str:
        """
        Encrypts a private key using the initialized encryption key.

        :param private_key: The private key as a string.
        :return: The encrypted private key as a string.
        """
        return self.cipher.encrypt(private_key.encode()).decode()

    def decrypt_private_key(self, encrypted_key: str) -> str:
        """
        Decrypts an encrypted private key.

        :param encrypted_key: The encrypted private key as a string.
        :return: The decrypted private key as a string.
        """
        return self.cipher.decrypt(encrypted_key.encode()).decode()

    def btc(self) -> tuple[str, str] | str:
        """
        Generates a Bitcoin (BTC) wallet address and private key.

        This method uses the Bitcoinlib library to create a wallet. It generates a unique wallet name using UUID,
        creates the wallet, and returns the wallet address and private key as strings. If any error occurs during
        wallet creation, it returns the error message.

        :return: A tuple containing the wallet address and private key as strings.
                 Returns an error message string in case of failure.
        """
        try:
            wallet_name = f'BTCWallet_{uuid.uuid4()}'  # Unique wallet name using UUID
            wallet = Wallet.create(wallet_name)  # Create a new Bitcoin wallet
            wallet_address = wallet.get_key().address
            private_key = wallet.get_key().key_private
            encrypted_key = self.encrypt_private_key(private_key.hex())
            return str(wallet_address), encrypted_key
        except WalletError as wallet_error:
            return str(wallet_error)

    def trx(self) -> tuple[str, str] | str:
        """
        Generates a Tron (TRX) wallet address and private key.

        This method creates a new Tron wallet using the Tronpy library. It generates a random private key and derives
        the public address from it. The method returns the wallet address and private key as hexadecimal strings.
        If any error occurs, it returns the error message.

        :return: A tuple containing the wallet address and private key as strings.
                 Returns an error message string in case of failure.
        """
        try:
            private_key = PrivateKey.random()  # Generate a random private key for Tron
            wallet_address = private_key.public_key.to_base58check_address()  # Convert public key to address
            encrypted_key = self.encrypt_private_key(private_key.hex())
            return str(wallet_address), encrypted_key
        except Exception as e:
            return str(e)

    def ton(self) -> tuple[str, str] | str:
        """
        Generates a TON (The Open Network) wallet address and private key.

        This method uses the TON SDK to create a wallet. It generates a random wallet with a specified version
        and workchain. The method returns the wallet address and private key as strings. If any error occurs,
        it returns the error message.

        :return: A tuple containing the wallet address and private key as strings.
                 Returns an error message string in case of failure.
        """
        try:
            # Create a TON wallet with version v3r2 and workchain 0
            mnemonics, pub_k, pri_k, wallet = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)
            encrypted_key = self.encrypt_private_key(pri_k.hex())
            return str(wallet.address.to_string(True, True, False, True)), encrypted_key
        except Exception as e:
            return str(e)

    def sol(self) -> tuple[str, str] | str:
        """
        Generates a Solana (SOL) wallet address and private key.

        This method creates a new Solana wallet using the Solana SDK. It generates a keypair, extracts the public key,
        and encodes the private key in base64. The method returns the public address and secret key. If an error occurs,
        the method will return the error message.

        :return: A tuple containing the wallet address and private key as strings.
                 Returns an error message string in case of failure.
        """
        try:
            keypair = Keypair.generate()  # Generate a new keypair for Solana
            public_key = keypair.public_key
            secret_key = base64.b64encode(keypair.secret_key).decode('utf-8')  # Encode the secret key in base64
            encrypted_key = self.encrypt_private_key(secret_key)
            return str(public_key), encrypted_key
        except Exception as e:
            return str(e)

    def eth(self) -> tuple[str, str] | str:
        """
        Generates an Ethereum (ETH) wallet address and private key.

        This method uses the Web3 library to create a new Ethereum account. It returns the public address and private key
        as hexadecimal strings. In case of any error during wallet creation, an error message is returned.

        :return: A tuple containing the wallet address and private key as strings.
                 Returns an error message string in case of failure.
        """
        try:
            account = Account.create()  # Create a new Ethereum account
            public_address = account.address
            private_key = account.key.hex()
            encrypted_key = self.encrypt_private_key(private_key)
            return public_address, encrypted_key
        except Exception as e:
            return str(e)


if __name__ == '__main__':
    w = WalletAddressGenerator()
    import json

    from functools import lru_cache


    @lru_cache(maxsize=None)
    async def ton_gen():
        list_addresses = []

        for i in range(1000):
            address = w.ton()[0][:42]
            list_addresses.append(address)
            print(f"Ton №{i} Address gener", address)

        with open("ton-addresses.json", "w") as f:
            json.dump(list_addresses, f, indent=4)

    import asyncio
    asyncio.run(ton_gen())
    