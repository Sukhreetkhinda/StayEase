import sqlite3

conn = sqlite3.connect("hotel_system.db")
cur = conn.cursor()

try:
    cur.execute("ALTER TABLE bookings ADD COLUMN total_cost REAL")
    print("Column 'total_cost' added successfully!")
except Exception as e:
    print("Error:", e)

conn.commit()
conn.close()
