import sqlite3
import os
instance_path = os.path.join(os.getcwd(), "instance", "patients.db")
local_path = os.path.join(os.getcwd(), "patients.db")
db_path = instance_path if os.path.exists(instance_path) else local_path
if not os.path.exists(db_path):
    print("Database file not found.")
    print("Run the application first and add at least one patient record.")
    exit()
try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("=" * 60)
    print(f"DATABASE OVERVIEW ({os.path.basename(db_path)})")
    print("=" * 60)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    if not tables:
        print("No tables found in database.")
        exit()
    for table_name in tables:
        print("\n" + "=" * 60)
        print(f"TABLE: {table_name.upper()}")
        print("=" * 60)
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [column[1] for column in cursor.fetchall()]
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        if not rows:
            print("No records found.")
            continue
        for row in rows:
            print("-" * 60)
            for column_name, value in zip(columns, row):
                print(f"{column_name}: {value}")
    print("\n" + "=" * 60)
    print("Database reading completed.")
except Exception as e:
    print(f"Error: {e}")
finally:
    if "conn" in locals():
        conn.close()
