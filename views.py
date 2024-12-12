# from flask import Blueprint, render_template, request, redirect, url_for
# from functions import add_donor, get_all_donors, get_donor_by_id, update_donor, delete_donor

# routes = Blueprint('routes', __name__)


# @routes.route('/')
# def index():
#     donors = get_all_donors()
#     return render_template('index.html', donors=donors)


# @routes.route('/add', methods=['GET', 'POST'])
# def add_donor_route():
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         blood_group = request.form['blood_group']
#         last_donated = request.form['last_donated']

#         add_donor(name, age, blood_group, last_donated)
#         return redirect(url_for('routes.index'))

#     return render_template('add_donor.html')


# @routes.route('/update/<int:id>', methods=['GET', 'POST'])
# def update_donor_route(id):
#     donor = get_donor_by_id(id)

#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         blood_group = request.form['blood_group']
#         last_donated = request.form['last_donated']

#         update_donor(donor, name, age, blood_group, last_donated)
#         return redirect(url_for('routes.index'))

#     return render_template('update_donor.html', donor=donor)


# @routes.route('/delete/<int:id>', methods=['POST'])
# def delete_donor_route(id):
#     donor = get_donor_by_id(id)
#     delete_donor(donor)
#     return redirect(url_for('routes.index'))

# --------------------------------------------------------------------------------------------
# from flask import Blueprint, request, jsonify
# from db import Database
# from models import fetch_all_donors, fetch_blood_inventory
# from functions import add_donation, update_blood_inventory

# views = Blueprint("views", __name__)

# @views.route("/", methods=["GET"])
# def home():
#     return "Welcome to the Blood Donation System API. Use /donors, /blood-bank, or /donate routes."

# @views.route("/favicon.ico", methods=["GET"])
# def favicon():
#     return "", 204


# @views.route("/donors", methods=["GET"])
# def get_donors():
#     db = Database()
#     donors = fetch_all_donors(db)
#     db.close()
#     return jsonify(donors)

# @views.route("/blood-bank", methods=["GET"])
# def get_blood_bank():
#     db = Database()
#     inventory = fetch_blood_inventory(db)
#     db.close()
#     return jsonify(inventory)

# @views.route("/donate", methods=["POST"])
# def donate_blood():
#     data = request.json
#     donor_id = data.get("donor_id")
#     donation_date = data.get("donation_date")
#     donation_amount = data.get("donation_amount")
#     blood_type = data.get("blood_type")

#     db = Database()
#     add_donation(db, donor_id, donation_date, donation_amount)
#     update_blood_inventory(db, blood_type, 1)
#     db.close()

#     return jsonify({"message": "Donation added and inventory updated successfully!"}), 201




from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from db import Database
from models import fetch_all_donors, fetch_blood_inventory
from functions import add_donation, update_blood_inventory

views = Blueprint('views', __name__)

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
