from flask import Blueprint, render_template, request  # Added request to imports

# Define the Blueprint
routes = Blueprint('routes', __name__)

@routes.route('/add', methods=['GET', 'POST'])
def add_donor_route():
    if request.method == 'POST':  # Check if the method is POST
        donor_name = request.form['donor_name']  # Get form data
        donor_age = request.form['donor_age']
        blood_group = request.form['blood_group']
        
        # Example: Add the donor logic here
        # Save to the database or handle logic
        # db.add_donor(donor_name, donor_age, blood_group)

        return "Donor added successfully!"  # Or redirect to another page

    # Render the add donor form for GET requests
    return render_template('add_donor.html')
