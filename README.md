📌 Project Description

A complete QR-Based Student Verification System built using Python, Flask, and Excel. This project automatically generates QR codes for each student and provides a secure web-based verification system to check their payment status.

🧩 Features

📄 Reads student data directly from students.xlsx

🎨 Generates unique QR codes using Enrollment Numbers

🌐 Flask web app to verify scanned QR codes

🔐 Secure HTTPS support using SSL certificates

✅ Shows Name, Enrollment No., Section & Payment Status

🗂️ Saves all QR codes neatly in a dedicated folder

🛠️ Tech Stack

Python

Flask

Pandas

OpenPyXL

QRCode

If you want, I can also give you a short version or the full README.md for your repo 💙

You said:
 350 characters
ChatGPT said:

Here’s a crisp, clean 350-character description with emojis, buddy:

📌 A Python-Flask based QR verification system that generates QR codes from Excel student data and securely verifies them via a web interface. 🎫 Uses pandas for data handling, HTTPS for secure access, and provides instant checks for name, enrollment, section, and payment status. 🔐✨

You said:
now make a readme
ChatGPT said:

Absolutely, my friend — here’s a clean, professional, and GitHub-ready README.md for your full QR project.
It’s polished, easy to read, and perfect for recruiters too.
(Includes emojis, but kept classy and not overdone.)

QR-Based Student Verification System 🎫🔐

A complete Python + Flask solution for generating and verifying student QR codes.
The system creates unique QR codes from Excel data and securely verifies each student’s payment status via a web interface.

🚀 Features

📄 Reads student details from students.xlsx

🎨 Generates unique QR codes using Enrollment Numbers

🌐 Web-based verification using Flask

🔐 HTTPS support with cert.pem and key.pem

⚡ Instant verification: Name, Enrollment, Section & Payment Status

🗂 Saves all generated QR codes automatically

📁 Project Structure
📦 QR Verification Project
├── app.py                # Flask verification app
├── app checker.py        # Environment test script
├── Qr Checker.py         # QR generation script
├── students.xlsx         # Student data
├── cert.pem              # SSL certificate
├── key.pem               # SSL private key
└── qrcodes/              # Auto-generated QR code images

🛠️ Tech Stack

Python 3

Flask

Pandas

OpenPyXL

qrcode

HTML/CSS (for frontend)

📦 Installation

Make sure Python is installed.

1️⃣ Install Dependencies
pip install flask pandas openpyxl qrcode

2️⃣ Place your student Excel file

Make sure the file is named:

students.xlsx


It must contain columns like:

Enrollment_No

Name

Paid

Section

🔧 Generating QR Codes

Run the generator script:

python "Qr Checker.py"


This will:

Load students.xlsx

Create QR codes for each student

Save them inside qrcodes/

🌐 Running the Verification Server

Start the Flask web app with HTTPS:

python app.py


The server starts at:

https://localhost:5000


Now, you can scan a QR code → it will verify whether the student has paid.

🧪 API Endpoint
POST /verify

Example payload:

{
  "enrolment": "123456789"
}


Response:

"allowed" if paid

"not_paid" if not paid

"invalid" if enrolment not found

🛡️ Security

HTTPS enabled for safe transfer 🔐

Certificates: cert.pem & key.pem

Local use recommended

📜 License

This project is licensed under the MIT License.

💙 Author

Created with dedication and curiosity — always improving and learning!
