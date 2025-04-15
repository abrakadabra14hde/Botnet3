import sqlite3
import os

class UserDatabase:
    def __init__(self, db_path='database/users.db'):
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def connect(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def create_table_user(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                username TEXT,
                subscription_end DATE
            )
        ''')
        self.connection.commit()
