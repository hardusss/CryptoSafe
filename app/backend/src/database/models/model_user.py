from app.backend.src.database.db_connection import Database


class ModelUser:
    """This class creates a table users"""
    def __init__(self, db: Database) -> None:
        self.db = db
        self.cursor = db.cursor

    def create_table(self) -> None:
        """
        Create table in database crypto_safe
        Columns
        chat_id: unique identifier for Telegram chat
        username: Telegram username
        first_name: Telegram first name
        last_name: Telegram last name
        language_code: Telegram language code
        registration_date: datetime when user joined Telegram chat
        last_activity: datetime when user last active in Telegram chat
        usdt_balance: user's USDT balance
        usdt_wallet_address: user's USDT wallet address
        btc_balance: user's BTC balance
        btc_wallet_address: user's BTC wallet address
        eth_balance: user's ETH balance
        eth_wallet_address: user's ETH wallet address
        ton_balance: user's TON balance
        ton_wallet_address: user's TON wallet address
        status: user's status (active, inactive, banned)
        transaction_history: JSON object with transaction history
        :return None
        """
        query_create = """
            create table if not exists users (
                chat_id BIGINT PRIMARY KEY,
                username VARCHAR(50),
                first_name VARCHAR(100),
                last_name VARCHAR(100),
                language_code VARCHAR(10),
                registration_date DATETIME,
                last_activity DATETIME,
                usdt_balance DECIMAL(18, 8) DEFAULT 0.0, 
                usdt_wallet_address VARCHAR(255), 
                btc_balance DECIMAL(18, 8) DEFAULT 0.0, 
                btc_wallet_address VARCHAR(255), 
                eth_balance DECIMAL(18, 8) DEFAULT 0.0, 
                eth_wallet_address VARCHAR(255), 
                ton_balance DECIMAL(18, 8) DEFAULT 0.0, 
                ton_wallet_address VARCHAR(255), 
                status VARCHAR(20) DEFAULT 'active',
                transaction_history JSON, 
                INDEX (chat_id)
            )
        """
        try:
            self.cursor.execute(query_create)
            print("Table created successfully...")
            self.db.close()
        except Exception as e:
            print(f"Error creating table: {str(e)}")
            self.db.close()


if __name__ == '__main__':
    db = Database()
    model_user = ModelUser(db=db)
    model_user.create_table()

