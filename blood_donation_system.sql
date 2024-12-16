# CREATE DATABASE blood_donation_system;
# USE blood_donation_system;
#
# CREATE TABLE donors (
#     donor_id INT AUTO_INCREMENT PRIMARY KEY,
#     first_name VARCHAR(50) NOT NULL,
#     last_name VARCHAR(50) NOT NULL,
#     date_of_birth DATE NOT NULL,
#     blood_type ENUM('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-') NOT NULL,
#     contact_number VARCHAR(15),
#     email VARCHAR(100),
#     address TEXT,
#     last_donated DATE
# );
#
# CREATE TABLE donations (
#     donation_id INT AUTO_INCREMENT PRIMARY KEY,
#     donor_id INT,
#     donation_date DATE,
#     donation_amount INT,  -- Amount in ml (typically 450ml per donation)
#     FOREIGN KEY (donor_id) REFERENCES donors(donor_id)
# );
#
# CREATE TABLE blood_bank (
#     blood_type ENUM('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-') PRIMARY KEY,
#     total_units INT DEFAULT 0  -- The amount of blood available for each blood type
# );
#
# CREATE TABLE appointments (
#     appointment_id INT AUTO_INCREMENT PRIMARY KEY,
#     donor_id INT,
#     appointment_date DATETIME,
#     status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
#     FOREIGN KEY (donor_id) REFERENCES donors(donor_id)
# );
#
# INSERT INTO blood_bank (blood_type, total_units) VALUES
# ('A+', 0),
# ('A-', 0),
# ('B+', 0),
# ('B-', 0),
# ('O+', 0),
# ('O-', 0),
# ('AB+', 0),
# ('AB-', 0);
#
# INSERT INTO donors (first_name, last_name, date_of_birth, blood_type, contact_number, email, address)
# VALUES
# ('John', 'Doe', '1985-04-15', 'O+', '1234567890', 'john@example.com', '123 Main Street'),
# ('Jane', 'Smith', '1990-07-22', 'A-', '9876543210', 'jane.smith@example.com', '456 Elm Street'),
# ('Alice', 'Johnson', '1982-11-10', 'B+', '5551234567', 'alice.johnson@example.com', '789 Oak Avenue'),
# ('Bob', 'Brown', '1995-03-05', 'AB-', '5557654321', 'bob.brown@example.com', '101 Pine Road'),
# ('Charlie', 'Davis', '1978-09-30', 'O-', '5559876543', 'charlie.davis@example.com', '202 Maple Lane');
#
#
# INSERT INTO appointments (donor_id, appointment_date, status)
# VALUES
# (1, '2024-12-15 10:00:00', 'Scheduled'),
# (2, '2024-12-16 09:30:00', 'Scheduled'),
# (3, '2024-12-17 14:00:00', 'Scheduled'),
# (4, '2024-12-18 11:15:00', 'Scheduled'),
# (5, '2024-12-19 16:45:00', 'Scheduled');
#
# INSERT INTO donations (donor_id, donation_date, donation_amount)
# VALUES
# (1, '2024-12-15', 450),
# (2, '2024-12-16', 450),
# (3, '2024-12-17', 450),
# (4, '2024-12-18', 450),
# (5, '2024-12-19', 450);
#
# UPDATE blood_bank
# SET total_units = total_units + 1
# WHERE blood_type = 'O+';
#
# SELECT * FROM donors;
#
# SELECT * FROM donations WHERE donor_id = 1;
#
# SELECT * FROM blood_bank;
#
# SELECT blood_type, SUM(donation_amount) AS total_donated
# FROM donations
# JOIN donors ON donations.donor_id = donors.donor_id
# GROUP BY blood_type;
#
# SELECT a.appointment_id, d.first_name, d.last_name, a.appointment_date
# FROM appointments a
# JOIN donors d ON a.donor_id = d.donor_id
# WHERE a.status = 'Scheduled' AND a.appointment_date > NOW();
#
#
# SHOW DATABASES;
# USE blood_donation_system;
#
# SELECT DATABASE();
#
# SHOW TABLES;
# SELECT * FROM donors;
#
#
