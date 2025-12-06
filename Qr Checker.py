import pandas as pd
import qrcode
import os

print(" Loading Excel file...")

try:
    df = pd.read_excel("students.xlsx")
    print(" Excel file loaded successfully!")
except Exception as e:
    print(" Error loading Excel file:", e)
    exit()

# Check if DataFrame is empty
if df.empty:
    print(" The Excel file is empty! Please add student data.")
    exit()

# Show first few rows for confirmation
print(" First rows of data:")
print(df.head())

# Create folder for QR codes
os.makedirs("qrcodes", exist_ok=True)

print("Generating QR codes...")
for index, row in df.iterrows():
    enrollment = str(row["Enrollment_No"])
    name = row["Name"].replace(" ", "_")  # safe filename

    qr = qrcode.make(enrollment)

    filename = f"qrcodes/{enrollment}_{name}.png"
    qr.save(filename)

    print(f" QR generated for {row['Name']} ({enrollment}) -> {filename}")

print(" All QR codes generated! Check the 'qrcodes' folder.")
