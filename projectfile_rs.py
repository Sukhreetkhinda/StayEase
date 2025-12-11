
########################TRIAL#############################################

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import database  # CHANGED: Was 'db'
from tkinter import simpledialog
import subprocess  # ADDED: To open other .py files
from session import set_user_email

# 🔹 Email imports (for welcome mail + OTP)
from email_config import SENDER_EMAIL, SENDER_PASSWORD
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# # ---------- EMAIL CONFIG ----------
# SENDER_EMAIL = "khindasukhreet@gmail.com"        # 👉 put your Gmail here
# SENDER_PASSWORD = "lybk nuor gjyr ywt"   # 👉 your Gmail App Password

# global store for OTP (simple for single-user desktop app)
current_otp = None
current_otp_email = None

# ------------ Helper: send welcome email on login ------------
def send_login_email(to_email, user_name):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = "Welcome back to Rosemount Residencies"

    body = f"""Dear {user_name},

You have successfully logged into Rosemount Residencies.

We’re happy to host you again. If you face any issue with your booking,
feel free to contact the front desk.

Warm regards,
Rosemount Residencies
"""
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)  # 👈 uses shared config
        server.send_message(msg)
        server.quit()
    except Exception as e:
        # Show *info* but don’t fail login
        messagebox.showinfo(
            "Login Email",
            f"Login successful, but email could not be sent:\n{e}"
        )


# ------------ Helper: send OTP email ------------
def send_otp_email(to_email, otp):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = "Password Reset OTP - Rosemount Residencies"

    body = f"""Dear Guest,

Your OTP for resetting your password is: {otp}

Please use this OTP to complete your password reset. 
Do not share this code with anyone.

Regards,
Rosemount Residencies
"""
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()

# ------------ Forgot Password Flow ------------
def forgot_password():
    global current_otp, current_otp_email

    # Step 1: Ask for registered email
    email = simpledialog.askstring("Forgot Password", "Enter your registered email:")
    if not email:
        return

    # Check if email exists in users table
    try:
        conn = sqlite3.connect("hotel_system.db")
        cur = conn.cursor()
        cur.execute("SELECT name FROM users WHERE email = ?", (email,))
        row = cur.fetchone()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"Database error:\n{e}")
        return

    if not row:
        messagebox.showerror("Error", "No user found with this email.")
        return

    user_name = row[0]

    # Step 2: Generate OTP and send email
    try:
        otp = random.randint(100000, 999999)
        current_otp = str(otp)
        current_otp_email = email
        send_otp_email(email, current_otp)
        messagebox.showinfo("OTP Sent", f"An OTP has been sent to:\n{email}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not send OTP email:\n{e}")
        return

    # Step 3: Ask for OTP
    entered_otp = simpledialog.askstring("OTP Verification", "Enter the OTP sent to your email:")
    if not entered_otp:
        return

    if entered_otp.strip() != current_otp:
        messagebox.showerror("Error", "Invalid OTP. Please try again.")
        return

    # Step 4: Ask for new password
    new_pass = simpledialog.askstring("Reset Password", "Enter new password:", show="*")
    if not new_pass:
        return
    confirm_pass = simpledialog.askstring("Reset Password", "Confirm new password:", show="*")
    if not confirm_pass:
        return

    if new_pass != confirm_pass:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    # Step 5: Update password in DB
    try:
        conn = sqlite3.connect("hotel_system.db")
        cur = conn.cursor()
        cur.execute("UPDATE users SET password = ? WHERE email = ?", (new_pass, current_otp_email))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Password updated successfully. You can now login.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not update password:\n{e}")
        return


# ------MAIN WINDOW---------
root = tk.Tk()
root.title("Rosemount Residencies - Login/Register")
root.geometry("1000x700")
root.resizable(False, False)

#------------menu bar------------
from menu_bar import add_menu
add_menu(root)

# --------- BACKGROUND IMAGE ---------
bg_image = Image.open("green and white.jpg").resize((1000, 700))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# --------- MAIN FRAME ---------
main_frame = tk.Frame(root, bg="white")
main_frame.place(x=150, y=100, width=700, height=500)

#------------menu bar------------
from menu_bar import add_menu
add_menu(root)

# ---------LEFT IMAGE PANEL---------
left_image = Image.open("rmlogo1.png").resize((350, 500))
left_photo = ImageTk.PhotoImage(left_image)
tk.Label(main_frame, image=left_photo).place(x=0, y=0, width=350, height=500)

# ---------RIGHT SIDE FRAMES ---------
login_frame = tk.Frame(main_frame, bg="#144272")
register_frame = tk.Frame(main_frame, bg="#144272")
home_frame = tk.Frame(root)

for frame in (login_frame, register_frame):
    frame.place(x=350, y=0, width=350, height=500)

#---------WELCOME LABEL IN HOME FRAME---------
welcome_label = tk.Label(home_frame, text="", font=("Arial", 20, "bold"), fg="#0b5d81", justify="center")
welcome_label.pack(pady=30)

#---------NAVIGATION FUNCTIONS ---------
def show_register():
    login_frame.place_forget()
    home_frame.place_forget()
    register_frame.place(x=350, y=0, width=450, height=500)

def show_login():
    register_frame.place_forget()
    home_frame.place_forget()
    login_frame.place(x=350, y=0, width=350, height=500)

# --------- REGISTER FUNCTION ---------
def register():
    name = reg_name.get()
    email = reg_email.get()
    password = reg_pass.get()
    confirm = reg_confirm.get()

    if not name or not email or not password or not confirm:
        messagebox.showerror("Error", "All fields are required.")
    elif password != confirm:
        messagebox.showerror("Error", "Passwords do not match.")
    else:
        try:
            database.add_user(name, email, password)
            messagebox.showinfo("Success", "Registration successful!")
            show_login()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already registered.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

#--------- LOGIN FUNCTION ---------
def login():
    email = login_email.get()
    password = login_pass.get()

    conn = sqlite3.connect('hotel_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users WHERE email = ? AND password = ?", (email, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        user_name = result[0]
        messagebox.showinfo("Success", f"Welcome, {user_name}!")

        set_user_email(email)

        # 🔹 Try sending welcome email (non-blocking idea: no threading for now)
        send_login_email(email, user_name)

        root.destroy()
        subprocess.Popen(["python", "home.py"])

    else:
            messagebox.showerror("Error", "Invalid email or password")

# --------- admin ---------
def admin_login_passkey():
    root.destroy()
    subprocess.Popen(["python", "admin.py"])

# --------- REGISTER FRAME UI ---------
tk.Label(register_frame, text="REGISTER", font=("Arial", 20, "bold"), bg="#144272", fg="white").place(x=100, y=20)
tk.Label(register_frame, text="Name", font=("Arial", 12, "bold"), bg="#144272", fg="white").place(x=40, y=70)
reg_name = tk.Entry(register_frame,  font=("Arial", 12), fg="white", bg="#144272", insertbackground='white',highlightbackground="white", highlightthickness=1, bd=0)
reg_name.place(x=40, y=100,width=250, height=25)
tk.Label(register_frame, text="Email", font=("Arial", 12, "bold"), bg="#144272", fg="white").place(x=40, y=130)
reg_email = tk.Entry(register_frame, font=("Arial", 12), fg="white", bg="#144272", insertbackground='white',highlightbackground="white", highlightthickness=1, bd=0)
reg_email.place(x=40, y=160,width=250, height=25)
tk.Label(register_frame, text="Password", font=("Arial", 12, "bold"), bg="#144272", fg="white").place(x=40, y=195)
reg_pass = tk.Entry(register_frame, font=("Arial", 12), fg="white", bg="#144272", insertbackground='white',highlightbackground="white", highlightthickness=1, bd=0, show="*")
reg_pass.place(x=40, y=225,width=250, height=25)
tk.Label(register_frame, text="Confirm Password", font=("Arial", 12, "bold"), bg="#144272", fg="white").place(x=40, y=260)
reg_confirm = tk.Entry(register_frame, font=("Arial", 12), fg="white", bg="#144272", insertbackground='white',highlightbackground="white", highlightthickness=1, bd=0, show="*")
reg_confirm.place(x=40, y=290,width=250, height=25)
tk.Button(register_frame, text="REGISTER", bg="white", fg="#144272", font=("Arial", 12, "bold"),command=register, bd=0).place(x=100, y=340, width=150)
tk.Button(register_frame, text="Already registered? Login", font=("Arial", 10), bg="#144272", fg="white",bd=0, command=show_login).place(x=90, y=380)
tk.Button(register_frame, text="Admin? Go to Admin Page", font=("Arial", 10), bg="#144272", fg="white", bd=0, command=admin_login_passkey).place(x=90, y=410)

# --------- LOGIN FRAME UI ---------
tk.Label(login_frame, text="LOGIN", font=("Arial", 22, "bold"), bg="#144272", fg="white").place(x=120, y=30)
tk.Label(login_frame, text="Email", font=("Arial", 12, "bold"), bg="#144272", fg="white").place(x=40, y=100)
login_email = tk.Entry(login_frame, font=("Arial", 12), fg="white", bg="#144272", insertbackground='white',highlightbackground="white", highlightthickness=1, bd=0)
login_email.place(x=40, y=130,width=250, height=25)
tk.Label(login_frame, text="Password", font=("Arial", 12, "bold"), bg="#144272", fg="white").place(x=40, y=180)
login_pass = tk.Entry(login_frame, font=("Arial", 12), fg="white", bg="#144272", insertbackground='white',highlightbackground="white", highlightthickness=1, bd=0, show="*")
login_pass.place(x=40, y=210,width=250, height=25)

tk.Button(login_frame, text="ENTER", bg="white", fg="#144272", font=("Arial", 12, "bold"),command=login, bd=0).place(x=100, y=270, width=150)

# 🔹 New: Forgot Password button (same style, no layout change to others)
tk.Button(login_frame, text="Forgot Password?", font=("Arial", 10), bg="#144272", fg="white",
          bd=0, command=forgot_password).place(x=110, y=310)

tk.Button(login_frame, text="New user? Register", font=("Arial", 10), bg="#144272", fg="white",bd=0, command=show_register).place(x=110, y=340)

# --------- DATABASE CONNECT---------
database.connect_db()  # This will create the tables if they don't exist

# --------- START---------
show_register()
root.mainloop()
