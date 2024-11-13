import mysql.connector
from dotenv import load_dotenv
from os import getenv


class Database:
    def __init__(self) -> None:
        """
        Initialize the database connection
        """
        load_dotenv()
        try:
            self.connection = mysql.connector.connect(
                host=getenv('DB_HOST'),
                user=getenv('DB_USER'),
                password=getenv('DB_PASSWORD'),
                database=getenv('DB_NAME')
            )
            self.cursor = self.connection.cursor()
            print('Connected to the MySQL database...')

        except Exception as error:
            print(f"Error connecting to the database: {error}")

    def close(self):
        """Closed connection with the MySQL database"""
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Connection to the MySQL database closed.")
