# from db import db

# class Donor(db.Model):
#     __tablename__ = 'donors'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     blood_type = db.Column(db.String(5), nullable=False)
#     last_donation_date = db.Column(db.Date, nullable=True)
#     age = db.Column(db.Integer, nullable=False)  # New age field added

def fetch_all_donors(db):
    query = "SELECT * FROM donors"
    return db.execute(query).fetchall()

def fetch_blood_inventory(db):
    query = "SELECT * FROM blood_bank"
    return db.execute(query).fetchall()

def fetch_donor_appointments(db, donor_id):
    query = "SELECT * FROM appointments WHERE donor_id = %s"
    return db.execute(query, (donor_id,)).fetchall()