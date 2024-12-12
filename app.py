# # test_db_connection.py
# from mysql.connector import Error
# import mysql.connector


# # app.py
# from flask import Flask
# from db import db  # Import db from db.py
# from models import Donor
# from views import routes
# from flask_migrate import Migrate 

# app = Flask(__name__)
# app.register_blueprint(routes)
# migrate = Migrate(app, db)
# # Database URI - Update this with your credentials
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:12345678@localhost/flaskdb'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize SQLAlchemy with the Flask app
# db.init_app(app)  # Initialize db with the app


# # Test the connection
# @app.route('/')
# def index():
#     try:
#         # You can add this to test if the db is accessible
#         db.create_all()
#         return "Successfully connected to the database!"
#     except Exception as e:
#         return f"Failed to connect to the database. Error: {e}"
# def create_db_connection():
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             database='blood_donation_system',
#             user='root',
#             password='12345678'
#         )
#         if connection.is_connected():
#             print("Successfully connected to the database")
#             return connection
#         else:
#             print("Failed to connect to the database")
#             return None
#     except Error as e:
#         print(f"Error: {e}")
#         return None

# if __name__ == "__main__":
#     with app.app_context():
#         try:
#             print("Initializing database connection...")
#             # Test database connection here (optional but can help)
#             connection = create_db_connection()  # You can add this to check DB connection
#             if connection:
#                 print("Database connection successful.")
            
#             print("Creating tables...")
#             db.create_all()  # Create tables
#             print("Tables created successfully!")
#         except Exception as e:
#             print(f"Error while creating tables: {e}")
#     app.run(debug=True)

from flask import Flask
from views import views  # Import the views Blueprint
from routes import routes  # Import the routes Blueprint
from db_config import Config  # Import your configuration class

# Create the Flask app instance
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Register the Blueprints
app.register_blueprint(views)  # No URL prefix
app.register_blueprint(routes, url_prefix='/routes')  # URL prefix for routes Blueprint

# Define a default route
@app.route('/')
def home():
    return "Welcome to the Blood Donation System!"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
