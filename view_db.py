import sqlite3
import os

# Locate the database file
instance_path = os.path.join(os.getcwd(), 'instance', 'patients.db')
local_path = os.path.join(os.getcwd(), 'patients.db')
db_path = instance_path if os.path.exists(instance_path) else local_path

if not os.path.exists(db_path):
    print("❌ Critical Error: Could not find any 'patients.db' file!")
    print("Make sure you run 'python app.py' and interact with the site first.")
    exit()

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [t[0] for t in cursor.fetchall()]

    print("=" * 60)
    print(f"📁 DATABASE TRACKER OVERVIEW ({os.path.basename(db_path)})")
    print("=" * 60)

    # 1. DISPLAY ADMIN DATA
    print("\n🔐 [TABLE: USER] REGISTERED ADMIN ACCOUNTS:")
    print("-" * 60)
    if 'user' in tables:
        cursor.execute("SELECT id, username FROM user")
        admins = cursor.fetchall()
        if not admins:
            print("No admin accounts found.")
        for admin in admins:
            print(f"Admin ID: {admin[0]:<4} | Username: {admin[1]}")
    else:
        print("❌ Error: 'user' table does not exist yet.")

    # 2. DISPLAY PATIENTS DATA
    print("\n [TABLE: PATIENT] REGISTERED PATIENTS:")
    print("-" * 60)
    if 'patient' in tables:
        cursor.execute("SELECT id, full_name, email, remarks, admin_username FROM patient")
        patients = cursor.fetchall()
        if not patients:
            print("No patient records found.")
        for p in patients:
            print(f"ID: {p[0]:<3} | Name: {p[1]:<15} | Email: {p[2]:<20}")
            print(f"     ↳ AI Remarks: {p[3]}")
            print(f"     ↳ Added By Admin: '{p[4]}'")
            print("." * 60)
    else:
        print("❌ Error: 'patient' table does not exist yet.")

    print("\n" + "=" * 60)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'conn' in locals():
        conn.close()