# # functions.py
# from models import Donor
# from db import db

# def add_donor(name, age, blood_type, last_donated):
#     """Add a new donor to the database."""
#     new_donor = Donor(name=name, blood_type=blood_type, last_donation_date=last_donated, age=age)
#     db.session.add(new_donor)
#     db.session.commit()


# def get_all_donors():
#     """Get all donors from the database."""
#     return Donor.query.all()

# def get_donor_by_id(donor_id):
#     """Get a donor by ID."""
#     return Donor.query.get_or_404(donor_id)

# def update_donor(donor, name, age, blood_group, last_donated):
#     """Update donor details."""
#     donor.name = name
#     donor.age = age
#     donor.blood_group = blood_group
#     donor.last_donated = last_donated
#     db.session.commit()

# def delete_donor(donor):
#     """Delete a donor."""
#     db.session.delete(donor)
#     db.session.commit()


def add_donation(db, donor_id, donation_date, donation_amount):
    query = """
    INSERT INTO donations (donor_id, donation_date, donation_amount)
    VALUES (%s, %s, %s)
    """
    db.execute(query, (donor_id, donation_date, donation_amount))
    db.commit()




def add_donor(db, first_name, last_name, date_of_birth, blood_type, last_donated):
    query = """
    INSERT INTO donors (first_name, last_name, date_of_birth, blood_type, last_donated)
    VALUES (%s, %s, %s, %s, %s)
    """
    db.execute(query, (first_name, last_name, date_of_birth, blood_type, last_donated))
    db.commit()




def update_blood_inventory(db, blood_type, units):
    query = """
    UPDATE blood_bank SET total_units = total_units + %s
    WHERE blood_type = %s
    """
    db.execute(query, (units, blood_type))
    db.commit()

