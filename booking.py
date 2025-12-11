#############################triAl###########################################

import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry     # ✅ Calendar added without changing UI
from database import connect_db
import sqlite3
from datetime import datetime
import subprocess
from session import get_user_email


def init_booking_table():
    try:
        conn = sqlite3.connect("hotel_system.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                user_email TEXT,
                room_type TEXT,
                check_in TEXT,
                check_out TEXT,
                guests INTEGER,
                rooms INTEGER,
                days INTEGER,
                total_amount REAL NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        print("✅ Booking table initialized successfully.")
    except Exception as e:
        print(f"⚠️ Error initializing booking table: {e}")


# ------------ ROOM RATES -------------
ROOM_RATES = {
    "Single": 1500,
    "Double": 2500,
    "Deluxe": 4000,
    "Suite": 7000
}

# ------------ TOTAL ROOMS (for availability display) ------------
TOTAL_ROOMS = {
    "Single": 10,
    "Double": 8,
    "Deluxe": 5,
    "Suite": 3
}

# ------------ EXTRA CHARGES -------------
CLEANING_CHARGE = 100               # fixed per booking
SERVICE_CHARGE_PER_NIGHT = 50       # per night

# Add-on prices (you can change these if you want)
ADDON_PRICES = {
    "Airport Pickup": 500,
    "Extra Breakfast": 200,
    "Extra Bed": 400,
}


# ------------ CALCULATE DAYS ----------
def calculate_days():
    try:
        in_date = datetime.strptime(entry_checkin.get(), "%d-%m-%Y")
        out_date = datetime.strptime(entry_checkout.get(), "%d-%m-%Y")
        days = (out_date - in_date).days

        if days <= 0:
            messagebox.showerror("Error", "Check-out must be after Check-in!")
            return 0

        return days
    except:
        return 0


# ------------ AVAILABLE ROOMS COUNTER ----------
def update_available_rooms(*args):
    room_type = room_var.get()
    total = TOTAL_ROOMS.get(room_type, 0)

    left = total
    try:
        conn = connect_db()
        cur = conn.cursor()
        # Sum of rooms already booked for this type
        cur.execute("SELECT COALESCE(SUM(rooms), 0) FROM bookings WHERE room_type = ?", (room_type,))
        booked = cur.fetchone()[0] or 0
        conn.close()
        left = max(total - booked, 0)
    except Exception as e:
        print("⚠️ Could not fetch availability:", e)

    available_label_var.set(f"{room_type} Rooms Left: {left}")


# ------------ CALCULATE COST ----------
def calculate_cost(*args):
    room_type = room_var.get()
    rooms = int(room_count_var.get())
    days = calculate_days()

    total = 0

    # Base room cost
    if room_type in ROOM_RATES and days > 0:
        total = ROOM_RATES[room_type] * rooms * days

    # Cleaning + service charges
    if days > 0:
        total += CLEANING_CHARGE                  # one-time
        total += SERVICE_CHARGE_PER_NIGHT * days  # per night

    # Add-on charges
    addons_total = 0
    if addon_airport_var.get() == 1:
        addons_total += ADDON_PRICES["Airport Pickup"]
    if addon_breakfast_var.get() == 1:
        addons_total += ADDON_PRICES["Extra Breakfast"]
    if addon_extra_bed_var.get() == 1:
        addons_total += ADDON_PRICES["Extra Bed"]

    total += addons_total

    # Update cost entry
    entry_cost.delete(0, tk.END)
    if total > 0:
        entry_cost.insert(0, str(total))

    # Also refresh availability (in case room type just changed)
    update_available_rooms()


# ------------ SAVE BOOKING ----------
def save_booking():
    name = entry_name.get()
    user_email = get_user_email()
    room_type = room_var.get()
    check_in = entry_checkin.get()
    check_out = entry_checkout.get()
    guests = entry_guests.get()
    rooms = room_count_var.get()
    days = calculate_days()
    total_cost = entry_cost.get()
    
    # Convert total_cost to float and map to total_amount for DB
    try:
        total_amount = float(total_cost)
    except:
        messagebox.showerror("Error", "Invalid total cost value.")
        return


    # days = calculate_days()
    # total_cost = entry_cost.get()

    if not (name and room_type and check_in and check_out and guests and total_cost):
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO bookings (name, user_email, room_type, check_in, check_out, guests, rooms, days, total_amount)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (name, user_email, room_type, check_in, check_out, guests, rooms, days, total_amount))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Booking Confirmed Successfully!")
    window.destroy()
    subprocess.Popen(["python", "room_service.py"])


# ---------------- UI -----------------
window = tk.Tk()
window.title("Room Booking - Hotel Booking System")
window.geometry("500x560")
window.config(bg="#e6f2ff")

#------------menu bar------------
from menu_bar import add_menu
add_menu(window)

tk.Label(window, text=" 🏨 HOTEL BOOKING SYSTEM", font=("Arial", 18, "bold"),
         bg="#e6f2ff", fg="#004080").pack(pady=20)
tk.Label(window, text="Room Booking", font=("Arial", 14), bg="#e6f2ff").pack(pady=10)

frame = tk.Frame(window, bg="#e6f2ff")
frame.pack(pady=10)

# Full Name
tk.Label(frame, text="Full Name:", bg="#e6f2ff").grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=0, column=1, pady=5)

# Room Type
tk.Label(frame, text="Room Type:", bg="#e6f2ff").grid(row=1, column=0, sticky="w", pady=5)
room_var = tk.StringVar(value="Single")
room_list = ["Single", "Double", "Deluxe", "Suite"]

def on_room_change(*_):
    calculate_cost()
    update_available_rooms()

menu_room = tk.OptionMenu(frame, room_var, *room_list, command=lambda _: on_room_change())
menu_room.grid(row=1, column=1, pady=5)

# Check-in Date WITH DATE FORMAT + CALENDAR
tk.Label(frame, text="Check-in Date (dd-mm-yyyy):", bg="#e6f2ff").grid(row=2, column=0, sticky="w", pady=5)
entry_checkin = DateEntry(frame, width=27, date_pattern="dd-mm-yyyy")
entry_checkin.grid(row=2, column=1, pady=5)

# Check-out Date WITH DATE FORMAT + CALENDAR
tk.Label(frame, text="Check-out Date (dd-mm-yyyy):", bg="#e6f2ff").grid(row=3, column=0, sticky="w", pady=5)
entry_checkout = DateEntry(frame, width=27, date_pattern="dd-mm-yyyy")
entry_checkout.grid(row=3, column=1, pady=5)

# Bind cost recalculation when date changes
entry_checkin.bind("<<DateEntrySelected>>", calculate_cost)
entry_checkout.bind("<<DateEntrySelected>>", calculate_cost)

# Guests
tk.Label(frame, text="Guests:", bg="#e6f2ff").grid(row=4, column=0, sticky="w", pady=5)
entry_guests = tk.Entry(frame, width=30)
entry_guests.grid(row=4, column=1, pady=5)

# Number of Rooms
tk.Label(frame, text="Rooms:", bg="#e6f2ff").grid(row=5, column=0, sticky="w", pady=5)
room_count_var = tk.IntVar(value=1)
spin_rooms = tk.Spinbox(frame, from_=1, to=10, textvariable=room_count_var,
                        width=5, command=calculate_cost)
spin_rooms.grid(row=5, column=1, pady=5, sticky="w")

# ✅ Available Rooms label (under Rooms)
available_label_var = tk.StringVar(value="")
available_label = tk.Label(frame, textvariable=available_label_var,
                           bg="#e6f2ff", fg="#004080", font=("Arial", 9, "bold"))
available_label.grid(row=6, column=1, sticky="w", pady=(2, 6))

# ✅ Add-ons
tk.Label(frame, text="Add-ons:", bg="#e6f2ff").grid(row=7, column=0, sticky="nw", pady=5)

addon_airport_var = tk.IntVar(value=0)
addon_breakfast_var = tk.IntVar(value=0)
addon_extra_bed_var = tk.IntVar(value=0)

cb_airport = tk.Checkbutton(
    frame, text="Airport Pickup", bg="#e6f2ff",
    variable=addon_airport_var, command=calculate_cost
)
cb_airport.grid(row=7, column=1, sticky="w")

cb_breakfast = tk.Checkbutton(
    frame, text="Extra Breakfast", bg="#e6f2ff",
    variable=addon_breakfast_var, command=calculate_cost
)
cb_breakfast.grid(row=8, column=1, sticky="w")

cb_extra_bed = tk.Checkbutton(
    frame, text="Extra Bed", bg="#e6f2ff",
    variable=addon_extra_bed_var, command=calculate_cost
)
cb_extra_bed.grid(row=9, column=1, sticky="w")

# Total Cost (Auto-Calculated)
tk.Label(frame, text="Total Cost (₹):", bg="#e6f2ff").grid(row=10, column=0, sticky="w", pady=5)
entry_cost = tk.Entry(frame, width=30)
entry_cost.grid(row=10, column=1, pady=5)

# Buttons
tk.Button(window, text="Confirm Booking", command=save_booking,
          bg="#0073e6", fg="white", width=20).pack(pady=20)
tk.Button(window, text="Back to Room Info", bg="#e6f2ff", fg="#004080",
          borderwidth=0,
          command=lambda: [window.destroy(), subprocess.Popen(["python", "room_info.py"])])\
    .pack(pady=15)

init_booking_table()

# Let the window draw first, THEN query DB for available rooms
window.after(200, update_available_rooms)

window.mainloop()
