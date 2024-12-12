#import mysql.connector
#from mysql.connector import Error


# MySQL database connection setup
#def create_db_connection():
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

class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "12345678")
    DB_NAME = "blood_donation_system"
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")