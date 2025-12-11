# import sqlite3

# # Create / connect to database
# def connect_db():
#     conn = sqlite3.connect("hotel.db")
#     cur = conn.cursor()
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     ''')
#     conn.commit()
#     conn.close()

# def insert_user(name, email, password):
#     conn = sqlite3.connect("hotel.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
#     conn.commit()
#     conn.close()

# def fetch_all_users():
#     conn = sqlite3.connect("hotel.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM users")
#     data = cur.fetchall()
#     conn.close()
#     return data

# def delete_user(user_id):
#     conn = sqlite3.connect("hotel.db")
#     cur = conn.cursor()
#     cur.execute("DELETE FROM users WHERE id=?", (user_id,))
#     conn.commit()
#     conn.close()

# def update_user(user_id, name, email, password):
#     conn = sqlite3.connect("hotel.db")
#     cur = conn.cursor()
#     cur.execute("UPDATE users SET name=?, email=?, password=? WHERE id=?", (name, email, password, user_id))
#     conn.commit()
#     conn.close()


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# import sqlite3

# # --- Connect to Database ---
# def connect_db():
#     return sqlite3.connect("hotel_management.db")

# # --- Create Users Table ---
# def create_table():
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)
#     conn.commit()
#     conn.close()

# # --- Insert User ---
# def insert_user(name, email, password):
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
#         (name, email, password)
#     )
#     conn.commit()
#     conn.close()

# # --- Fetch User for Login ---
# def fetch_user(email, password):
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute(
#         "SELECT * FROM users WHERE email = ? AND password = ?",
#         (email, password)
#     )
#     user = cursor.fetchone()
#     conn.close()
#     return user

# # --- Initialize Table Automatically ---
# create_table()











# import sqlite3

# # ---------------------------------------------
# # DATABASE CONNECTION FUNCTION
# # ---------------------------------------------
# def connect_db():
#     try:
#         conn = sqlite3.connect("hotel_system.db", timeout=10)
#         return conn
#     except sqlite3.Error as e:
#         print("Database connection error:", e)
#         return None


# # ---------------------------------------------
# # CREATE ALL REQUIRED TABLES
# # ---------------------------------------------
# def create_tables():
#     conn = connect_db()
#     if conn is None:
#         print("❌ Database connection failed.")
#         return

#     cursor = conn.cursor()

#     # ---------------- USERS TABLE ----------------
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)

#     # ---------------- BOOKINGS TABLE ----------------
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS bookings (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER,
#             name TEXT NOT NULL,
#             room_type TEXT NOT NULL,
#             checkin_date TEXT NOT NULL,
#             checkout_date TEXT NOT NULL,
#             guests INTEGER,
#             total_amount REAL,
#             FOREIGN KEY (user_id) REFERENCES users (id)
#         )
#     """)

#     # ---------------- PAYMENTS TABLE ----------------
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS payments (
#             payment_id TEXT PRIMARY KEY,
#             user_id INTEGER,
#             name TEXT NOT NULL,
#             amount REAL NOT NULL,
#             status TEXT NOT NULL,
#             date TEXT,
#             FOREIGN KEY (user_id) REFERENCES users (id)
#         )
#     """)

#     # ---------------- ROOM SERVICE TABLE ----------------
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS room_service (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER,
#             room_no TEXT,
#             item TEXT,
#             quantity INTEGER,
#             price REAL,
#             status TEXT DEFAULT 'Pending',
#             FOREIGN KEY (user_id) REFERENCES users (id)
#         )
#     """)

#     # ---------------- ADMIN LOG TABLE (Optional) ----------------
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS admin_log (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             action TEXT,
#             timestamp TEXT
#         )
#     """)

#     conn.commit()
#     conn.close()
#     print("✅ All tables created successfully.")


# # ---------------------------------------------
# # INSERT FUNCTIONS (OPTIONAL EXAMPLES)
# # ---------------------------------------------
# def insert_user(name, email, password):
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
#     conn.commit()
#     conn.close()


# def insert_booking(user_id, name, room_type, checkin, checkout, guests, total_cost):
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("""
#         INSERT INTO bookings (user_id, name, room_type, checkin_date, checkout_date, guests, total_cost)
#         VALUES (?, ?, ?, ?, ?, ?, ?)
#     """, (user_id, name, room_type, checkin, checkout, guests, total_cost))
#     conn.commit()
#     conn.close()


# def insert_payment(payment_id, user_id, name, amount, status, date):
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("""
#         INSERT INTO payments (payment_id, user_id, name, amount, status, date)
#         VALUES (?, ?, ?, ?, ?, ?)
#     """, (payment_id, user_id, name, amount, status, date))
#     conn.commit()
#     conn.close()


# def insert_room_service(user_id, room_no, item, quantity, price):
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("""
#         INSERT INTO room_service (user_id, room_no, item, quantity, price)
#         VALUES (?, ?, ?, ?, ?)
#     """, (user_id, room_no, item, quantity, price))
#     conn.commit()
#     conn.close()


# # ---------------------------------------------
# # RUN THIS FILE ONCE TO CREATE TABLES
# # ---------------------------------------------
# if __name__ == "__main__":
#     create_tables()



















##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@########################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



# import sqlite3

# # ========== DATABASE CONNECTION ==========
# def connect_db():
#     """Connect to the SQLite database and create all required tables if they don't exist."""
#     conn = sqlite3.connect("hotel_system.db")
#     cur = conn.cursor()

#     # ========== USERS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)

#     # ========== BOOKINGS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS bookings (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_email TEXT NOT NULL,
#             room_type TEXT NOT NULL,
#             check_in TEXT NOT NULL,
#             check_out TEXT NOT NULL,
#             total_amount REAL NOT NULL,
#             status TEXT DEFAULT 'Confirmed',
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     # ========== ROOM SERVICE TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS room_service (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_email TEXT NOT NULL,
#             room_no TEXT,
#             service_type TEXT NOT NULL,
#             status TEXT DEFAULT 'Pending',
#             cost REAL DEFAULT 0,
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     # ========== PAYMENTS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS payments (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_email TEXT NOT NULL,
#             amount REAL NOT NULL,
#             method TEXT NOT NULL,
#             payment_date TEXT NOT NULL,
#             status TEXT DEFAULT 'Completed',
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     conn.commit()
#     conn.close()


# # ========== INSERT FUNCTIONS (OPTIONAL) ==========
# def add_user(name, email, password):
#     conn = sqlite3.connect("hotel_system.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
#     conn.commit()
#     conn.close()


# def add_booking(user_email, room_type, check_in, check_out, total_amount):
#     conn = sqlite3.connect("hotel_system.db")
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO bookings (user_email, room_type, check_in, check_out, total_amount) VALUES (?, ?, ?, ?, ?)",
#         (user_email, room_type, check_in, check_out, total_amount),
#     )
#     conn.commit()
#     conn.close()


# def add_room_service(user_email, room_no, service_type, cost):
#     conn = sqlite3.connect("hotel_system.db")
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO room_service (user_email, room_no, service_type, cost) VALUES (?, ?, ?, ?)",
#         (user_email, room_no, service_type, cost),
#     )
#     conn.commit()
#     conn.close()


# def add_payment(user_email, amount, method, payment_date):
#     conn = sqlite3.connect("hotel_system.db")
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO payments (user_email, amount, method, payment_date) VALUES (?, ?, ?, ?)",
#         (user_email, amount, method, payment_date),
#     )
#     conn.commit()
#     conn.close()


# # ========== MAIN EXECUTION ==========
# if __name__ == "__main__":
#     connect_db()
#     print("✅ Hotel Management Database initialized successfully!")





####################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# import sqlite3

# # ========== DATABASE CONNECTION ==========
# def connect_db():
#     """Connect to the SQLite database and create all required tables if they don't exist."""
#     conn = sqlite3.connect("hotel_system.db")
#     cur = conn.cursor()

#     # ========== USERS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)

#     # ========== BOOKINGS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS bookings (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_email TEXT NOT NULL,
#             room_type TEXT NOT NULL,
#             check_in TEXT NOT NULL,
#             check_out TEXT NOT NULL,
#             total_amount REAL NOT NULL,
#             status TEXT DEFAULT 'Confirmed',
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     # ========== ROOM SERVICE TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS room_service (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_email TEXT NOT NULL,
#             room_no TEXT,
#             service_type TEXT NOT NULL,
#             status TEXT DEFAULT 'Pending',
#             cost REAL DEFAULT 0,
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     # ========== PAYMENTS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS payments (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_email TEXT NOT NULL,
#             amount REAL NOT NULL,
#             method TEXT NOT NULL,
#             payment_date TEXT NOT NULL,
#             status TEXT DEFAULT 'Completed',
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     conn.commit()
#     return conn  # ✅ Return connection for reuse in other modules


# # ========== INSERT FUNCTIONS (OPTIONAL) ==========
# def add_user(name, email, password):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
#     conn.commit()
#     conn.close()


# def add_booking(user_email, room_type, check_in, check_out, total_amount):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO bookings (user_email, room_type, check_in, check_out, total_amount) VALUES (?, ?, ?, ?, ?)",
#         (user_email, room_type, check_in, check_out, total_amount),
#     )
#     conn.commit()
#     conn.close()


# def add_room_service(user_email, room_no, service_type, cost):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO room_service (user_email, room_no, service_type, cost) VALUES (?, ?, ?, ?)",
#         (user_email, room_no, service_type, cost),
#     )
#     conn.commit()
#     conn.close()


# def add_payment(user_email, amount, method, payment_date):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO payments (user_email, amount, method, payment_date) VALUES (?, ?, ?, ?)",
#         (user_email, amount, method, payment_date),
#     )
#     conn.commit()
#     conn.close()


# # ========== MAIN EXECUTION ==========
# if __name__ == "__main__":
#     conn = connect_db()
#     conn.close()
#     print("✅ Hotel Management Database initialized successfully!")




#######################################################################################################################



# import sqlite3

# # ========== DATABASE CONNECTION ==========
# def connect_db():
#     """Connect to the SQLite database and create all required tables if they don't exist."""
#     conn = sqlite3.connect("hotel_system.db")
#     cur = conn.cursor()

#     # ========== USERS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)

#     # ========== BOOKINGS TABLE (UPDATED) ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS bookings (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             user_email TEXT NOT NULL,
#             room_type TEXT NOT NULL,
#             check_in TEXT NOT NULL,
#             check_out TEXT NOT NULL,
#             guests INTEGER DEFAULT 1,
#             total_amount REAL NOT NULL,
#             status TEXT DEFAULT 'Confirmed',
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     # ========== ROOM SERVICE TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS room_service (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_email TEXT NOT NULL,
#             room_no TEXT,
#             service_type TEXT NOT NULL,
#             status TEXT DEFAULT 'Pending',
#             cost REAL DEFAULT 0,
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     # ========== PAYMENTS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS payments (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_email TEXT ,
#             amount REAL ,
#             method TEXT ,
#             payment_date TEXT ,
#             status TEXT DEFAULT 'Completed',
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     conn.commit()
#     return conn  # ✅ Return connection for reuse in other modules


# # ========== INSERT FUNCTIONS ==========
# def add_user(name, email, password):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
#     conn.commit()
#     conn.close()


# def add_booking(name, user_email, room_type, check_in, check_out, guests, total_cost):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO bookings (name, user_email, room_type, check_in, check_out, guests, total_cost) VALUES (?, ?, ?, ?, ?, ?, ?)",
#         (name, user_email, room_type, check_in, check_out, guests, total_cost),
#     )
#     conn.commit()
#     conn.close()


# def add_room_service(user_email, room_no, service_type, cost):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO room_service (user_email, room_no, service_type, cost) VALUES (?, ?, ?, ?)",
#         (user_email, room_no, service_type, cost),
#     )
#     conn.commit()
#     conn.close()


# def add_payment(user_email, amount, method, payment_date):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO payments (user_email, amount, method, payment_date) VALUES (?, ?, ?, ?)",
#         (user_email, amount, method, payment_date),
#     )
#     conn.commit()
#     conn.close()


# # ========== MAIN EXECUTION ==========
# if __name__ == "__main__":
#     conn = connect_db()
#     conn.close()
#     print("✅ Hotel Management Database initialized successfully!")




####################################workingggggggg gooodddd#########################################

# import sqlite3
# import os

# # ========== DATABASE CONNECTION ==========
# def connect_db():
#     """Connect to the SQLite database and create all required tables if they don't exist."""
#     db_path = os.path.join(os.path.dirname(__file__), "hotel_system.db")
#     conn = sqlite3.connect(db_path)
#     cur = conn.cursor()

#     # ========== USERS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)

#     # ========== BOOKINGS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS bookings (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             user_email TEXT NOT NULL,
#             room_type TEXT NOT NULL,
#             check_in TEXT NOT NULL,
#             check_out TEXT NOT NULL,
#             guests INTEGER DEFAULT 1,
#             total_amount REAL NOT NULL,
#             status TEXT DEFAULT 'Confirmed',
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     # ✅ Add missing columns (rooms, days)
#     add_column_if_missing(cur, "bookings", "rooms", "INTEGER DEFAULT 1")
#     add_column_if_missing(cur, "bookings", "days", "INTEGER DEFAULT 1")

#     # ========== ROOM SERVICE TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS room_service (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_email TEXT NOT NULL,
#             room_no TEXT,
#             service_type TEXT NOT NULL,
#             status TEXT DEFAULT 'Pending',
#             cost REAL DEFAULT 0,
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     # ========== PAYMENTS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS payments (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_email TEXT,
#             amount REAL,
#             method TEXT,
#             payment_date TEXT,
#             status TEXT DEFAULT 'Completed',
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     conn.commit()
#     return conn  # ✅ Return connection for reuse in other modules


# # ========== COLUMN CHECK HELPER ==========
# def add_column_if_missing(cur, table, column, definition):
#     """Adds a column to a table if it doesn't already exist."""
#     cur.execute(f"PRAGMA table_info({table})")
#     columns = [info[1] for info in cur.fetchall()]
#     if column not in columns:
#         print(f"🛠️ Adding missing column '{column}' to '{table}'...")
#         cur.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


# # ========== INSERT FUNCTIONS ==========
# def add_user(name, email, password):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
#     conn.commit()
#     conn.close()


# def add_booking(name, user_email, room_type, check_in, check_out, guests, total_cost):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute("""
#         INSERT INTO bookings (name, user_email, room_type, check_in, check_out, guests, total_amount)
#         VALUES (?, ?, ?, ?, ?, ?, ?)
#     """, (name, user_email, room_type, check_in, check_out, guests, total_cost))
#     conn.commit()
#     conn.close()


# def add_room_service(user_email, room_no, service_type, cost):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute("""
#         INSERT INTO room_service (user_email, room_no, service_type, cost)
#         VALUES (?, ?, ?, ?)
#     """, (user_email, room_no, service_type, cost))
#     conn.commit()
#     conn.close()


# def add_payment(user_email, amount, method, payment_date):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute("""
#         INSERT INTO payments (user_email, amount, method, payment_date)
#         VALUES (?, ?, ?, ?)
#     """, (user_email, amount, method, payment_date))
#     conn.commit()
#     conn.close()


# # ========== MAIN EXECUTION ==========
# if __name__ == "__main__":
#     conn = connect_db()
#     print("✅ Hotel Management Database verified and ready!")
#     conn.close()





####################################################################################

# import sqlite3
# import os

# def connect_db():
#     """Connect to the SQLite database and create all required tables if they don't exist."""
#     db_path = os.path.join(os.path.dirname(__file__), "hotel_system.db")
#     conn = sqlite3.connect(db_path)
#     cur = conn.cursor()

#     # ========== USERS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)

#     # ========== BOOKINGS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS bookings (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             user_email TEXT NOT NULL,
#             room_type TEXT NOT NULL,
#             check_in TEXT NOT NULL,
#             check_out TEXT NOT NULL,
#             guests INTEGER DEFAULT 1,
#             total_amount REAL NOT NULL,
#             status TEXT DEFAULT 'Confirmed',
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     # ✅ Add missing columns (rooms, days, created_at)
#     add_column_if_missing(cur, "bookings", "rooms", "INTEGER DEFAULT 1")
#     add_column_if_missing(cur, "bookings", "days", "INTEGER DEFAULT 1")
#     add_column_if_missing(cur, "bookings", "created_at", "TEXT DEFAULT (datetime('now'))")

#     # ========== ROOM SERVICE TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS room_service (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_email TEXT NOT NULL,
#             room_no TEXT,
#             service_type TEXT NOT NULL,
#             status TEXT DEFAULT 'Pending',
#             cost REAL DEFAULT 0,
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     # ========== PAYMENTS TABLE ==========
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS payments (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_email TEXT,
#             amount REAL,
#             method TEXT,
#             payment_date TEXT,
#             status TEXT DEFAULT 'Completed',
#             FOREIGN KEY (user_email) REFERENCES users(email)
#         )
#     """)

#     conn.commit()
#     return conn


# # ---------- Helper to Add Columns Safely ----------
# def add_column_if_missing(cur, table, column, definition):
#     cur.execute(f"PRAGMA table_info({table})")
#     columns = [info[1] for info in cur.fetchall()]
#     if column not in columns:
#         print(f"🛠️ Adding missing column '{column}' to '{table}'...")
#         cur.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")















#################################updatedddd ##################################


import sqlite3
import os

# ========== DATABASE CONNECTION ==========
def connect_db():
    """Connect to the SQLite database and create all required tables if they don't exist."""
    db_path = os.path.join(os.path.dirname(__file__), "hotel_system.db")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # ========== USERS TABLE ==========
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # ========== BOOKINGS TABLE ==========
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            user_email TEXT NOT NULL,
            room_type TEXT NOT NULL,
            check_in TEXT NOT NULL,
            check_out TEXT NOT NULL,
            guests INTEGER DEFAULT 1,
            total_amount REAL NOT NULL,
            status TEXT DEFAULT 'Confirmed',
            FOREIGN KEY (user_email) REFERENCES users(email)
        )
    """)

    # ✅ Add missing columns (rooms, days)
    add_column_if_missing(cur, "bookings", "rooms", "INTEGER DEFAULT 1")
    add_column_if_missing(cur, "bookings", "days", "INTEGER DEFAULT 1")

    # ========== ROOM SERVICE TABLE ==========
    cur.execute("""
        CREATE TABLE IF NOT EXISTS room_service (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT NOT NULL,
            customer_name TEXT,
            item TEXT,
            room_no TEXT,
            service_type TEXT NOT NULL,
            status TEXT DEFAULT 'Pending',
            cost REAL DEFAULT 0,
            FOREIGN KEY (user_email) REFERENCES users(email)
        )
    """)

    # ✅ Ensure backward compatibility if table exists without new columns
    add_column_if_missing(cur, "room_service", "customer_name", "TEXT")
    add_column_if_missing(cur, "room_service", "item", "TEXT")

    # ========== PAYMENTS TABLE ==========
    cur.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT,
            amount REAL,
            method TEXT,
            payment_date TEXT,
            status TEXT DEFAULT 'Completed',
            FOREIGN KEY (user_email) REFERENCES users(email)
        )
    """)

    conn.commit()
    return conn  # ✅ Return connection for reuse in other modules


# ========== COLUMN CHECK HELPER ==========
def add_column_if_missing(cur, table, column, definition):
    """Adds a column to a table if it doesn't already exist."""
    cur.execute(f"PRAGMA table_info({table})")
    columns = [info[1] for info in cur.fetchall()]
    if column not in columns:
        print(f"🛠️ Adding missing column '{column}' to '{table}'...")
        cur.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


# ========== INSERT FUNCTIONS ==========
def add_user(name, email, password):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
    conn.commit()
    conn.close()


def add_booking(name, user_email, room_type, check_in, check_out, guests, total_cost):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO bookings (name, user_email, room_type, check_in, check_out, guests, total_amount)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, user_email, room_type, check_in, check_out, guests, total_cost))
    conn.commit()
    conn.close()


def add_room_service(user_email, room_no, service_type, cost):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO room_service (user_email, room_no, service_type, cost)
        VALUES (?, ?, ?, ?)
    """, (user_email, room_no, service_type, cost))
    conn.commit()
    conn.close()


def add_payment(user_email, amount, method, payment_date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO payments (user_email, amount, method, payment_date)
        VALUES (?, ?, ?, ?)
    """, (user_email, amount, method, payment_date))
    conn.commit()
    conn.close()


# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    conn = connect_db()
    print("✅ Hotel Management Database verified and ready!")
    conn.close()
