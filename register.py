# import tkinter as tk
# from tkinter import messagebox
# import sqlite3
# from db_config import connect_db

# def register_user():
#     username = entry_username.get()
#     password = entry_password.get()

#     if username == "" or password == "":
#         messagebox.showerror("Error", "All fields are required!")
#         return

#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
#     cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#     conn.commit()
#     conn.close()

#     messagebox.showinfo("Success", "Registration Successful!")
#     window.destroy()
#     import login

# def open_admin():
#     window.destroy()
#     import admin

# window = tk.Tk()
# window.title("Register - Hotel Booking System")
# window.geometry("600x600")
# window.config(bg="#e6f2ff")

# tk.Label(window, text="🏨 HOTEL BOOKING SYSTEM", font=("Arial", 16, "bold"), bg="#e6f2ff", fg="#004080").pack(pady=20)
# tk.Label(window, text="Register", font=("Arial", 14)).pack(pady=10)

# tk.Label(window, text="Username:", bg="#e6f2ff").pack(pady=5)
# entry_username = tk.Entry(window, width=30)
# entry_username.pack()

# tk.Label(window, text="Password:", bg="#e6f2ff").pack(pady=5)
# entry_password = tk.Entry(window, show="*", width=30)
# entry_password.pack()

# tk.Button(window, text="Register", command=register_user, bg="#0073e6", fg="white", width=20).pack(pady=15)
# tk.Button(window, text="Go to Admin Panel", command=open_admin, bg="#004080", fg="white", width=20).pack(pady=10)
# tk.Button(window, text="Already Registered? Login", command=lambda:[window.destroy(), __import__('login')], bg="#e6f2ff", fg="#004080", borderwidth=0).pack()

# window.mainloop()



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import subprocess
# from database import connect_db, insert_user

# connect_db()

# # --- Main Window ---
# root = tk.Tk()
# root.title("Rosemount Residencies - Register")
# root.geometry("1000x600")
# root.config(bg="white")

# # --- Left Side Image ---
# try:
#     img = Image.open("rmlogo1.png")  # your logo image
#     img = img.resize((450, 500))
#     photo = ImageTk.PhotoImage(img)
#     tk.Label(root, image=photo, bg="white").place(x=60, y=60)
# except:
#     tk.Label(root, text="Logo Not Found", bg="white", fg="grey").place(x=100, y=250)

# # --- Right Frame (Form Area) ---
# form_frame = tk.Frame(root, bg="#102A33", width=400, height=500)
# form_frame.place(x=520, y=60)

# tk.Label(form_frame, text="REGISTER", font=("Arial", 20, "bold"), bg="#102A33", fg="white").place(x=130, y=30)

# # Entries
# labels = ["Name", "Email", "Password", "Confirm Password"]
# entries = {}
# y_pos = 100
# for label in labels:
#     tk.Label(form_frame, text=label, font=("Arial", 10, "bold"), bg="#102A33", fg="white").place(x=60, y=y_pos)
#     entry = tk.Entry(form_frame, font=("Arial", 11), width=30, show="*" if "Password" in label else "")
#     entry.place(x=60, y=y_pos+25)
#     entries[label] = entry
#     y_pos += 70

# # Register Function
# def register_user():
#     name = entries["Name"].get()
#     email = entries["Email"].get()
#     password = entries["Password"].get()
#     confirm = entries["Confirm Password"].get()

#     if not name or not email or not password or not confirm:
#         messagebox.showwarning("Input Error", "All fields are required!")
#         return
#     if password != confirm:
#         messagebox.showerror("Error", "Passwords do not match!")
#         return

#     try:
#         insert_user(name, email, password)
#         messagebox.showinfo("Success", f"Welcome {name}! Registration successful.")
#     except Exception as e:
#         messagebox.showerror("Database Error", f"Error: {e}")

# tk.Button(form_frame, text="REGISTER", bg="white", fg="#102A33", font=("Arial", 11, "bold"), width=15, command=register_user).place(x=120, y=390)

# # --- Navigation Links ---
# tk.Label(form_frame, text="Already registered?", bg="#102A33", fg="white", font=("Arial", 9)).place(x=80, y=440)
# tk.Button(form_frame, text="Login", bg="#102A33", fg="lightblue", font=("Arial", 9, "underline"),
#           bd=0, cursor="hand2", command=lambda: subprocess.Popen(["python", "login.py"])).place(x=220, y=438)

# tk.Label(form_frame, text="Admin?", bg="#102A33", fg="white", font=("Arial", 9)).place(x=140, y=465)
# tk.Button(form_frame, text="Go to Admin Page", bg="#102A33", fg="lightblue", font=("Arial", 9, "underline"),
#           bd=0, cursor="hand2", command=lambda: subprocess.Popen(["python", "admin.py"])).place(x=190, y=463)

# root.mainloop()


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# from database import insert_user, create_table
# import subprocess

# # --- Create user table if not exists ---
# create_table()

# # --- Register Window ---
# def register_window():
#     win = tk.Tk()
#     win.title("Register - Hotel Management System")
#     win.geometry("900x600")
#     win.configure(bg="#0A2647")

#     # --- Background Image ---
#     try:
#         bg_img = Image.open("rmlogo1.png")  # background image
#         bg_img = bg_img.resize((900, 600))
#         bg = ImageTk.PhotoImage(bg_img)
#         bg_label = tk.Label(win, image=bg)
#         bg_label.place(x=0, y=0)
#     except:
#         pass  # if no image, continue with color background

#     # --- Register Frame ---
#     frame = tk.Frame(win, bg="white", width=400, height=450)
#     frame.place(relx=0.5, rely=0.5, anchor="center")

#     tk.Label(frame, text="REGISTER", font=("Arial", 22, "bold"), bg="white", fg="#0A2647").pack(pady=20)

#     # --- Entry fields ---
#     tk.Label(frame, text="Name:", font=("Arial", 12), bg="white").pack()
#     name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
#     name_entry.pack(pady=5)

#     tk.Label(frame, text="Email:", font=("Arial", 12), bg="white").pack()
#     email_entry = tk.Entry(frame, font=("Arial", 12), width=30)
#     email_entry.pack(pady=5)

#     tk.Label(frame, text="Password:", font=("Arial", 12), bg="white").pack()
#     password_entry = tk.Entry(frame, font=("Arial", 12), show="*", width=30)
#     password_entry.pack(pady=5)

#     # --- Register button ---
#     def register_user():
#         name = name_entry.get()
#         email = email_entry.get()
#         password = password_entry.get()

#         if name == "" or email == "" or password == "":
#             messagebox.showerror("Error", "All fields are required!")
#         else:
#             try:
#                 insert_user(name, email, password)
#                 messagebox.showinfo("Success", "Registered successfully!")
#             except Exception as e:
#                 messagebox.showerror("Error", f"Could not register user.\n{e}")

#     tk.Button(frame, text="Register", font=("Arial", 12, "bold"), bg="#0A2647", fg="white", width=15, command=register_user).pack(pady=15)

#     # --- Go to Login ---
#     def open_login():
#         win.destroy()  # close register window
#         subprocess.Popen(["python", "login.py"])  # open login.py in a new window

#     tk.Label(frame, text="Already have an account?", bg="white", font=("Arial", 10)).pack(pady=(15, 5))
#     tk.Button(frame, text="Login", font=("Arial", 11, "bold"), bg="#144272", fg="white", width=10, command=open_login).pack()

#     win.mainloop()


# if __name__ == "__main__":
#     register_window()


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import subprocess
# from database import insert_user, create_table

# create_table()

# def open_login():
#     import login
#     root.destroy()

# def register_user():
#     name = name_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     confirm = confirm_entry.get()

#     if not name or not email or not password or not confirm:
#         messagebox.showwarning("Input Error", "All fields are required!")
#         return
#     if password != confirm:
#         messagebox.showerror("Error", "Passwords do not match!")
#         return

#     try:
#         insert_user(name, email, password)
#         messagebox.showinfo("Success", f"Welcome {name}! Registration successful.")
#     except Exception as e:
#         messagebox.showerror("Database Error", f"Error: {e}")

# # --- Main Window ---
# root = tk.Tk()
# root.title("Rosemount Residencies - Register")
# root.geometry("900x600")
# root.config(bg="white")

# # --- Left Image Section ---
# try:
#     bg_img = Image.open("rmlogo1.png")
#     bg_img = bg_img.resize((450, 600))
#     bg_photo = ImageTk.PhotoImage(bg_img)
#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0)
# except:
#     tk.Label(root, text="Image not found", bg="white", fg="red", font=("Arial", 12)).place(x=100, y=250)

# # --- Right Form Frame ---
# form_frame = tk.Frame(root, bg="#102A43", width=450, height=600)
# form_frame.place(x=450, y=0)

# tk.Label(form_frame, text="REGISTER", bg="#102A43", fg="white",
#          font=("Arial", 20, "bold")).place(x=150, y=80)

# # --- Input Fields ---
# tk.Label(form_frame, text="Name", bg="#102A43", fg="white",
#          font=("Arial", 12)).place(x=80, y=160)
# name_entry = tk.Entry(form_frame, width=35, font=("Arial", 11))
# name_entry.place(x=80, y=185)

# tk.Label(form_frame, text="Email", bg="#102A43", fg="white",
#          font=("Arial", 12)).place(x=80, y=225)
# email_entry = tk.Entry(form_frame, width=35, font=("Arial", 11))
# email_entry.place(x=80, y=250)

# tk.Label(form_frame, text="Password", bg="#102A43", fg="white",
#          font=("Arial", 12)).place(x=80, y=290)
# password_entry = tk.Entry(form_frame, width=35, font=("Arial", 11), show="*")
# password_entry.place(x=80, y=315)

# tk.Label(form_frame, text="Confirm Password", bg="#102A43", fg="white",
#          font=("Arial", 12)).place(x=80, y=355)
# confirm_entry = tk.Entry(form_frame, width=35, font=("Arial", 11), show="*")
# confirm_entry.place(x=80, y=380)

# # --- Register Button ---
# tk.Button(form_frame, text="REGISTER", bg="white", fg="#102A43",
#           font=("Arial", 11, "bold"), width=15, command=register_user).place(x=150, y=430)

# # --- Navigation Links ---
# tk.Label(form_frame, text="Already registered?", bg="#102A43", fg="white",
#          font=("Arial", 9)).place(x=80, y=475)

# tk.Button(form_frame, text="Login", bg="#102A43", fg="lightblue",
#           font=("Arial", 9, "underline"), bd=0, cursor="hand2",
#           command=open_login).place(x=220, y=475)

# # --- Admin Access Link ---
# tk.Button(form_frame, text="Admin? Go to Admin Page", bg="#102A43", fg="lightblue",
#           font=("Arial", 9, "underline"), bd=0, cursor="hand2",
#           command=lambda: subprocess.Popen(["python", "admin.py"])).place(x=150, y=500)

# root.mainloop()



#$$$$$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import sqlite3
# import subprocess

# # ============= Database Setup =============
# def connect_db():
#     conn = sqlite3.connect("hotel_system.db")
#     cur = conn.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT,
#                     email TEXT UNIQUE,
#                     password TEXT)''')
#     conn.commit()
#     conn.close()

# def insert_user(name, email, password):
#     conn = sqlite3.connect("hotel_system.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
#     conn.commit()
#     conn.close()

# # ============= Register Window =============
# def register_window():
#     def register_user():
#         name = entry_name.get().strip()
#         email = entry_email.get().strip()
#         password = entry_password.get().strip()

#         if not name or not email or not password:
#             messagebox.showerror("Error", "All fields are required!")
#             return

#         try:
#             insert_user(name, email, password)
#             messagebox.showinfo("Success", "Registration successful!")
#             open_login()
#         except sqlite3.IntegrityError:
#             messagebox.showerror("Error", "Email already registered!")

#     def open_login():
#         win.destroy()
#         subprocess.Popen(["python", "login.py"])

#     def open_admin():
#         win.destroy()
#         subprocess.Popen(["python", "admin.py"])

#     connect_db()

#     win = tk.Tk()
#     win.title("Register - Hotel Management System")
#     win.geometry("900x600")
#     win.configure(bg="#0A2647")

#     # --- Background Image ---
#     try:
#         bg_img = Image.open("rmlogo1.png")
#         bg_img = bg_img.resize((900, 600))
#         bg_photo = ImageTk.PhotoImage(bg_img)
#         bg_label = tk.Label(win, image=bg_photo)
#         bg_label.place(x=0, y=0)
#     except:
#         win.configure(bg="#0A2647")

#     # --- Register Form Frame ---
#     form_frame = tk.Frame(win, bg="white", bd=2, relief="ridge")
#     form_frame.place(x=320, y=130, width=300, height=380)

#     tk.Label(form_frame, text="REGISTER", bg="white", fg="#102A43", font=("Arial", 18, "bold")).place(x=90, y=20)

#     tk.Label(form_frame, text="Name:", bg="white", fg="black", font=("Arial", 11)).place(x=30, y=80)
#     entry_name = tk.Entry(form_frame, font=("Arial", 11), bd=1, relief="solid")
#     entry_name.place(x=30, y=105, width=240)

#     tk.Label(form_frame, text="Email:", bg="white", fg="black", font=("Arial", 11)).place(x=30, y=145)
#     entry_email = tk.Entry(form_frame, font=("Arial", 11), bd=1, relief="solid")
#     entry_email.place(x=30, y=170, width=240)

#     tk.Label(form_frame, text="Password:", bg="white", fg="black", font=("Arial", 11)).place(x=30, y=210)
#     entry_password = tk.Entry(form_frame, font=("Arial", 11), bd=1, relief="solid", show="*")
#     entry_password.place(x=30, y=235, width=240)

#     tk.Button(form_frame, text="Register", bg="#102A43", fg="white", font=("Arial", 11, "bold"),
#               command=register_user).place(x=95, y=280, width=100, height=30)

#     # --- Login Link ---
#     tk.Label(form_frame, text="Already have an account?", bg="white", fg="black", font=("Arial", 9)).place(x=55, y=325)
#     tk.Button(form_frame, text="Login", bg="#102A43", fg="lightblue", font=("Arial", 9, "underline"),
#               bd=0, cursor="hand2", command=open_login).place(x=210, y=325)

#     # --- Admin Access Button ---
#     tk.Button(form_frame, text="Admin Login", bg="#102A43", fg="white", font=("Arial", 10, "bold"),
#               command=open_admin).place(x=90, y=350, width=120, height=28)

#     win.mainloop()

# if __name__ == "__main__":
#     register_window()





























################################################################################


# import tkinter as tk
# from tkinter import messagebox
# import sqlite3
# import subprocess

# def open_login():
#     root.destroy()
#     subprocess.Popen(["python", "login.py"])

# def open_admin():
#     root.destroy()
#     subprocess.Popen(["python", "admin.py"])

# def register_user():
#     name = entry_name.get()
#     email = entry_email.get()
#     password = entry_pass.get()

#     if not name or not email or not password:
#         messagebox.showerror("Error", "All fields are required!")
#         return

#     conn = sqlite3.connect("hotel_system.db")
#     cur = conn.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             email TEXT,
#             password TEXT
#         )
#     """)
#     cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
#                 (name, email, password))
#     conn.commit()
#     conn.close()

#     messagebox.showinfo("Success", "Registration successful!")
#     open_login()


# # -------- UI --------
# root = tk.Tk()
# root.title("Register")
# root.geometry("500x600")
# root.configure(bg="#EAF0F1")

# # Logo (if available)
# try:
#     from PIL import Image, ImageTk
#     logo = Image.open("rmlogo1.png")
#     logo = logo.resize((120, 120))
#     logo_img = ImageTk.PhotoImage(logo)
#     tk.Label(root, image=logo_img, bg="#EAF0F1").pack(pady=15)
# except:
#     pass

# tk.Label(root, text="Create an Account", font=("Arial", 20, "bold"), bg="#EAF0F1", fg="#0A2647").pack(pady=5)

# frame = tk.Frame(root, bg="#EAF0F1")
# frame.pack(pady=20)

# tk.Label(frame, text="Full Name", bg="#EAF0F1", fg="#0A2647", font=("Arial", 11, "bold")).grid(row=0, column=0, sticky="w")
# entry_name = tk.Entry(frame, width=35, font=("Arial", 11))
# entry_name.grid(row=1, column=0, pady=5)

# tk.Label(frame, text="Email", bg="#EAF0F1", fg="#0A2647", font=("Arial", 11, "bold")).grid(row=2, column=0, sticky="w", pady=(15,0))
# entry_email = tk.Entry(frame, width=35, font=("Arial", 11))
# entry_email.grid(row=3, column=0, pady=5)

# tk.Label(frame, text="Password", bg="#EAF0F1", fg="#0A2647", font=("Arial", 11, "bold")).grid(row=4, column=0, sticky="w", pady=(15,0))
# entry_pass = tk.Entry(frame, width=35, font=("Arial", 11), show="*")
# entry_pass.grid(row=5, column=0, pady=5)

# tk.Button(root, text="Register", width=20, bg="#0A2647", fg="white", font=("Arial", 11, "bold"),
#           command=register_user).pack(pady=15)

# tk.Button(root, text="Already have an account? Login", bg="#EAF0F1", fg="#144272",
#           font=("Arial", 10, "underline"), bd=0, command=open_login).pack()

# tk.Button(root, text="Admin Login", width=20, bg="#144272", fg="white",
#           font=("Arial", 11, "bold"), command=open_admin).pack(pady=20)

# root.mainloop()





##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#####################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import subprocess
import os

# --- Register Window ---
def open_register():
    root = tk.Tk()
    root.title("Rosemount Residencies - Register")
    root.geometry("900x600")
    root.configure(bg="white")
    root.resizable(False, False)

    def go_to_login():
        root.destroy()
        subprocess.Popen(["python", "login.py"])

    def go_to_admin():
        root.destroy()
        subprocess.Popen(["python", "admin.py"])

    def register_user():
        name = entry_name.get().strip()
        email = entry_email.get().strip()
        password = entry_pass.get().strip()
        confirm = entry_confirm.get().strip()

        if not name or not email or not password or not confirm:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        if password != confirm:
            messagebox.showwarning("Password Error", "Passwords do not match!")
            return

        try:
            conn = sqlite3.connect("hotel_system.db")
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            email TEXT UNIQUE,
                            password TEXT)''')
            cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                           (name, email, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration Successful!")
            go_to_login()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already exists!")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    # --- Left Side Image ---
    img = Image.open("rmlogo1.png")
    img = img.resize((370, 450))
    photo = ImageTk.PhotoImage(img)
    img_label = tk.Label(root, image=photo, bg="white")
    img_label.place(x=70, y=50)

    # --- Right Frame ---
    frame = tk.Frame(root, bg="#0b2e33", width=370, height=450)
    frame.place(x=430, y=52)
    
    #----resister text-------------
    title = tk.Label(frame, text="REGISTER", fg="white", bg="#0b2e33",
                     font=("Arial", 18, "bold"))
    title.place(x=110, y=40)

    #-----namelabels-----
    labels = ["Name", "Email", "Password", "Confirm Password"]
    entries = []
    y_pos = 90
    for label in labels:
        tk.Label(frame, text=label, bg="#0b2e33", fg="white",
                 font=("Arial", 10, "bold")).place(x=40, y=y_pos)
        entry = tk.Entry(frame, width=30, font=("Arial", 10), bd=1, relief="solid")
        entry.place(x=40, y=y_pos + 20)
        entries.append(entry)
        y_pos += 60

    entry_name, entry_email, entry_pass, entry_confirm = entries

    def on_hover(e):
        btn_register["bg"] = "#14464c"

    def on_leave(e):
        btn_register["bg"] = "white"

    btn_register = tk.Button(frame, text="REGISTER", font=("Arial", 10, "bold"),
                             bg="white", fg="#0b2e33", width=20, height=1,
                             bd=0, relief="flat", command=register_user)
    btn_register.place(x=70, y=330)
    btn_register.bind("<Enter>", on_hover)
    btn_register.bind("<Leave>", on_leave)

    tk.Label(frame, text="Already registered?", bg="#0b2e33", fg="white",
             font=("Arial", 9)).place(x=70, y=370)
    tk.Button(frame, text="Login", bg="#0b2e33", fg="skyblue", bd=0,
              cursor="hand2", command=go_to_login).place(x=180, y=370)

    tk.Label(frame, text="Admin?", bg="#0b2e33", fg="white",
             font=("Arial", 9)).place(x=70, y=390)
    tk.Button(frame, text="Go to Admin Page", bg="#0b2e33", fg="skyblue", bd=0,
              cursor="hand2", command=go_to_admin).place(x=120, y=390)

    root.mainloop()


if __name__ == "__main__":
    open_register()

