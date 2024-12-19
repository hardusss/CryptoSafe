from app.backend.src.database.db_connection import Database


class ModelUser:
    """This class manages tables for users, wallets, and balances."""
    def __init__(self, db: Database) -> None:
        self.db = db
        self.cursor = db.cursor

    def create_users_table(self) -> None:
        """Create users table."""
        query = """
        CREATE TABLE IF NOT EXISTS users (
            chat_id BIGINT PRIMARY KEY,
            username VARCHAR(50),
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            language_code VARCHAR(10) DEFAULT NULL,
            registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            last_activity DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            status VARCHAR(20) DEFAULT 'active',
            transaction_history JSON,
            INDEX (chat_id)
        );
        """
        self.cursor.execute(query)
        print("Users table created successfully.")

    def create_wallets_table(self) -> None:
        """Create wallets table."""
        query = """
            CREATE TABLE IF NOT EXISTS wallets (
            wallet_id INTEGER PRIMARY KEY auto_increment,
            chat_id BIGINT,
            wallet_type VARCHAR(5),
            address VARCHAR(255),
            encrypted_private_key TEXT,
            INDEX (chat_id),
            FOREIGN KEY (chat_id) REFERENCES users(chat_id) ON DELETE CASCADE ON UPDATE CASCADE,
        );
        """
        self.cursor.execute(query)
        print("Wallets table created successfully.")

    def create_all_tables(self) -> None:
        """Create all tables."""
        try:
            self.create_users_table()
            self.create_wallets_table()
            self.db.close()
        except Exception as e:
            print(f"Error creating tables: {str(e)}")
            self.db.close()


if __name__ == '__main__':
    db = Database()
    model_user = ModelUser(db=db)
    model_user.create_all_tables()
