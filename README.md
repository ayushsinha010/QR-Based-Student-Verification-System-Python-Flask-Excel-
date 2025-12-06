QR-Based Student Verification System

A Python and Flask based system for generating and verifying student QR codes. It reads student data from an Excel file, creates unique QR codes using enrollment numbers, and securely verifies each student’s payment status through a simple web interface.

Features:
Reads student details from students.xlsx
Generates unique QR codes for each student
Flask-based web verification system
HTTPS support with cert.pem and key.pem
Instant verification of name, enrollment, section, and payment status
Automatically saves all generated QR codes

Project Structure:
app.py – Flask verification app
app checker.py – environment test script
Qr Checker.py – QR generation script
students.xlsx – student data file
cert.pem – SSL certificate
key.pem – SSL key
qrcodes/ – folder containing generated QR images

Tech Stack:
Python, Flask, Pandas, OpenPyXL, qrcode

Installation:
Install required libraries: pip install flask pandas openpyxl qrcode
Place students.xlsx in the project folder with columns: Enrollment_No, Name, Paid, Section

Generating QR Codes:
Run the QR generator using: python Qr Checker.py
QR images will be saved to the qrcodes folder.

Running the Verification Server:
Start the Flask server using: python app.py
Visit https://localhost:5000
 to access the verification interface.

API Verification:
POST request to /verify with JSON containing enrolment.
Returns: allowed, not_paid, or invalid based on student data.

Security:
Uses HTTPS with SSL certificates for secure access.

License:
MIT License
