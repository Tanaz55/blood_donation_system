# # db.py
# from flask_sqlalchemy import SQLAlchemy

# # Initialize the SQLAlchemy object
# db = SQLAlchemy()


import mysql.connector
from db_config import Config

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()