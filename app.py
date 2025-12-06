from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load student data once at startup
students = pd.read_excel("students.xlsx")

# Normalize column names (remove spaces, lowercase)
students.columns = students.columns.str.strip().str.lower()
print("Excel Columns Normalized:", students.columns.tolist())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/verify", methods=["POST"])
def verify():
    data = request.json
    enrolment = data.get("enrolment")

    # Look up enrolment in Excel
    student = students[students["enrollment_no"].astype(str) == str(enrolment)]

    if not student.empty:
        student = student.iloc[0]
        paid_status = str(student["paid"]).strip().lower()

        if paid_status == "yes":
            print(f"[VERIFIED] {student['name']} ({student['enrollment_no']}) - ALLOWED")
            return jsonify({
                "status": "allowed",
                "name": student["name"],
                "enrolment": str(student["enrollment_no"]),  # ensure string
                "section": student["section"]
            })
        else:
            print(f"[VERIFIED] {student['name']} ({student['enrollment_no']}) - NOT PAID")
            return jsonify({
                "status": "not_paid",
                "name": student["name"],
                "enrolment": str(student["enrollment_no"]),
                "section": student["section"]
            })
    else:
        print(f"[FAILED] Enrolment {enrolment} not found")
        return jsonify({"status": "invalid"})

if __name__ == "__main__":
    # Run with HTTPS (requires cert.pem + key.pem in same folder)
    app.run(host="0.0.0.0", port=5000, ssl_context=("cert.pem", "key.pem"))
