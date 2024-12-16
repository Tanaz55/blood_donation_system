# import mysql.connector
# from mysql.connector import Error


# MySQL database connection setup
# def create_db_connection():
#    try:
#        connection = mysql.connector.connect(
#            host='localhost',
#            database='blood_donation_system',
#            user='root',
#           password='12345678'
#     )

#     if connection.is_connected():
#         print("Successfully connected to the database")
#         return connection
#     else:
#         print("Failed to connect to the database")
#         return None
# except Error as e:
#     print(f"Error: {e}")
#     return None


import os

import mysql.connector
from mysql.connector import Error
from flask import Flask

app = Flask(__name__)


# Load configuration
class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
    DB_NAME = "blood_donation_system"
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")


    @staticmethod
    def test_db_connection():
        try:
            connection = mysql.connector.connect(
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME,
            )
            if connection.is_connected():
                return "Database connection successful!"
        except Error as e:
            return f"Error: {e}"
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()

    def get_table_names():
        try:
            connection = mysql.connector.connect(
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME,
            )
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            table_names = [table[0] for table in tables]
            return table_names
        except Error as e:
            return f"Error: {e}"
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()

