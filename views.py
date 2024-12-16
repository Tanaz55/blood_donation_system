

import mysql.connector

from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify
from db import Database
from db_config import Config
from models import fetch_all_donors, fetch_blood_inventory
from functions import add_donation, update_blood_inventory
from functions import add_donor
import mysql.connector
from mysql.connector import Error

views = Blueprint('views', __name__)
app = Flask(__name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/donors')
def get_donors():
    db = Database()
    donors = fetch_all_donors(db)
    db.close()
    print(donors)  # Add this to debug the data
    return render_template('donors.html', donors=donors)


@views.route('/add_donor', methods=['POST', 'GET'])
def add_donors():
    if request.method == 'GET':
        # Render the template for the add donor form
        return render_template('add_donor.html')  # Ensure this points to your actual HTML file

    if request.method == 'POST':
        # Process form submission

        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            date_of_birth = request.form['date_of_birth']
            blood_type = request.form['blood_type']
            last_donated = request.form['last_donated']

            db = Database()
            add_donor(db, first_name, last_name, date_of_birth, blood_type, last_donated)
            db.close()

            return redirect(url_for('views.get_donors'))  # Adjust based on your setup

        except KeyError as e:
            # Handle missing fields gracefully
            return f"Missing field: {e}", 400


@views.route('/query_execute', methods=['GET'])
def query_execute():
    table_names = Config.get_table_names()
    return render_template('query_execute.html', table_names=table_names)


@views.route("/execute_query", methods=["POST"])
def execute_query():
    data = request.get_json()
    query = data.get("query")

    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
        )
        cursor = connection.cursor()
        cursor.execute(query)

        # Fetch column names and rows
        if cursor.description:  # Check if the query returns rows
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            return jsonify({"columns": columns, "rows": rows})
        else:
            connection.commit()  # For queries like INSERT, UPDATE, DELETE
            return jsonify({"columns": [], "rows": [["Query executed successfully!"]]}), 200

    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


@views.route('/blood-bank')
def get_blood_bank():
    db = Database()
    inventory = fetch_blood_inventory(db)
    db.close()
    return render_template('blood_bank.html', inventory=inventory)


@views.route('/donate', methods=['GET', 'POST'])
def donate_blood():
    if request.method == 'POST':
        donor_id = request.form['donor_id']
        donation_date = request.form['donation_date']
        donation_amount = request.form['donation_amount']
        blood_type = request.form['blood_type']

        db = Database()
        add_donation(db, donor_id, donation_date, donation_amount)
        update_blood_inventory(db, blood_type, 1)
        db.close()

        return redirect(url_for('views.get_blood_bank'))

    return render_template('donate.html')


@views.route('/get_columns/<table_name>', methods=['GET'])
def get_columns(table_name):
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
        )
        cursor = connection.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        columns = [row[0] for row in cursor.fetchall()]
        return jsonify(columns)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
