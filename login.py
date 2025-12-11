# import tkinter as tk
# from tkinter import messagebox
# from db_config import connect_db

# def login_user():
#     username = entry_username.get()
#     password = entry_password.get()

#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
#     result = cursor.fetchone()
#     conn.close()

#     if result:
#         messagebox.showinfo("Login Successful", f"Welcome {username}!")
#         window.destroy()
#         import home
#     else:
#         messagebox.showerror("Error", "Invalid Username or Password")

# window = tk.Tk()
# window.title("Login - Hotel Booking System")
# window.geometry("400x400")
# window.config(bg="#e6f2ff")

# tk.Label(window, text="🏨 HOTEL BOOKING SYSTEM", font=("Arial", 16, "bold"), bg="#e6f2ff", fg="#004080").pack(pady=20)
# tk.Label(window, text="Login", font=("Arial", 14)).pack(pady=10)

# tk.Label(window, text="Username:", bg="#e6f2ff").pack(pady=5)
# entry_username = tk.Entry(window, width=30)
# entry_username.pack()

# tk.Label(window, text="Password:", bg="#e6f2ff").pack(pady=5)
# entry_password = tk.Entry(window, show="*", width=30)
# entry_password.pack()

# tk.Button(window, text="Login", command=login_user, bg="#0073e6", fg="white", width=20).pack(pady=15)
# tk.Button(window, text="New User? Register", command=lambda:[window.destroy(), __import__('register')], bg="#e6f2ff", fg="#004080", borderwidth=0).pack()

# window.mainloop()



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import subprocess
# import sqlite3
# from database import connect_db

# connect_db()

# root = tk.Tk()
# root.title("Rosemount Residencies - Login")
# root.geometry("1000x600")
# root.config(bg="white")

# # --- Left Image ---
# try:
#     img = Image.open("rmlogo1.png")
#     img = img.resize((450, 500))
#     photo = ImageTk.PhotoImage(img)
#     tk.Label(root, image=photo, bg="white").place(x=60, y=60)
# except:
#     tk.Label(root, text="Logo Not Found", bg="white", fg="grey").place(x=100, y=250)

# # --- Right Frame ---
# frame = tk.Frame(root, bg="#102A33", width=400, height=500)
# frame.place(x=520, y=60)

# tk.Label(frame, text="LOGIN", font=("Arial", 20, "bold"), bg="#102A33", fg="white").place(x=150, y=40)

# tk.Label(frame, text="Email", font=("Arial", 10, "bold"), bg="#102A33", fg="white").place(x=60, y=120)
# email_entry = tk.Entry(frame, font=("Arial", 11), width=30)
# email_entry.place(x=60, y=150)

# tk.Label(frame, text="Password", font=("Arial", 10, "bold"), bg="#102A33", fg="white").place(x=60, y=210)
# password_entry = tk.Entry(frame, font=("Arial", 11), show="*", width=30)
# password_entry.place(x=60, y=240)

# # Login Function
# def login_user():
#     email = email_entry.get()
#     password = password_entry.get()

#     if not email or not password:
#         messagebox.showwarning("Input Error", "Please fill all fields.")
#         return

#     conn = sqlite3.connect("hotel.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
#     user = cur.fetchone()
#     conn.close()

#     if user:
#         messagebox.showinfo("Success", f"Welcome {email}!")
#         subprocess.Popen(["python", "home.py"])  # Optional redirect
#     else:
#         messagebox.showerror("Error", "Invalid email or password.")

# tk.Button(frame, text="ENTER", bg="white", fg="#102A33", font=("Arial", 11, "bold"), width=15, command=login_user).place(x=120, y=320)

# tk.Label(frame, text="New user?", bg="#102A33", fg="white", font=("Arial", 9)).place(x=130, y=370)
# tk.Button(frame, text="Register", bg="#102A33", fg="lightblue", font=("Arial", 9, "underline"),
#           bd=0, cursor="hand2", command=lambda: subprocess.Popen(["python", "register.py"])).place(x=190, y=368)

# root.mainloop()


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# from database import fetch_user

# def login_window():
#     win = tk.Tk()
#     win.title("Login - Hotel Management System")
#     win.geometry("900x600")
#     win.configure(bg="#0A2647")

#     # --- Background Image ---
#     try:
#         bg_img = Image.open("rmlogo1.png")
#         bg_img = bg_img.resize((900, 600))
#         bg = ImageTk.PhotoImage(bg_img)
#         bg_label = tk.Label(win, image=bg)
#         bg_label.place(x=0, y=0)
#     except:
#         pass

#     frame = tk.Frame(win, bg="white", width=400, height=400)
#     frame.place(relx=0.5, rely=0.5, anchor="center")

#     tk.Label(frame, text="LOGIN", font=("Arial", 22, "bold"), bg="white", fg="#0A2647").pack(pady=20)

#     tk.Label(frame, text="Email:", font=("Arial", 12), bg="white").pack()
#     email_entry = tk.Entry(frame, font=("Arial", 12), width=30)
#     email_entry.pack(pady=5)

#     tk.Label(frame, text="Password:", font=("Arial", 12), bg="white").pack()
#     password_entry = tk.Entry(frame, font=("Arial", 12), show="*", width=30)
#     password_entry.pack(pady=5)

#     def login():
#         email = email_entry.get()
#         password = password_entry.get()
#         user = fetch_user(email)

#         if user and user[3] == password:
#             messagebox.showinfo("Login Successful", f"Welcome, {user[1]}!")
#             win.destroy()
#             # You can import home.py here later
#         else:
#             messagebox.showerror("Error", "Invalid email or password")

#     tk.Button(frame, text="Login", font=("Arial", 12, "bold"), bg="#0A2647", fg="white", width=15, command=login).pack(pady=20)

#     win.mainloop()

# if __name__ == "__main__":
#     login_window()



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import sqlite3
# import subprocess

# # --- Function to open the Home Page after login ---
# def open_home():
#     messagebox.showinfo("Login Successful", "Welcome to Rosemount Residencies!")
#     root.destroy()
#     subprocess.Popen(["python", "home.py"])

# # --- Function to go to Register Page ---
# def open_register():
#     root.destroy()
#     subprocess.Popen(["python", "register.py"])

# # --- Function to Verify Login ---
# def verify_login():
#     email = email_entry.get()
#     password = password_entry.get()

#     if not email or not password:
#         messagebox.showwarning("Input Error", "Please enter both Email and Password")
#         return

#     try:
#         conn = sqlite3.connect("hotel.db")
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
#         result = cur.fetchone()
#         conn.close()

#         if result:
#             open_home()
#         else:
#             messagebox.showerror("Login Failed", "Invalid Email or Password")

#     except Exception as e:
#         messagebox.showerror("Database Error", f"Error: {e}")

# # --- Main Window ---
# root = tk.Tk()
# root.title("Rosemount Residencies - Login")
# root.geometry("900x600")
# root.config(bg="white")

# # --- Left Side Image ---
# try:
#     bg_img = Image.open("rmlogo1.png")
#     bg_img = bg_img.resize((450, 600))
#     bg_photo = ImageTk.PhotoImage(bg_img)
#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0)
# except:
#     tk.Label(root, text="Image not found", bg="white", fg="red", font=("Arial", 12)).place(x=100, y=250)

# # --- Right Side Login Form ---
# form_frame = tk.Frame(root, bg="#102A43", width=450, height=600)
# form_frame.place(x=450, y=0)

# tk.Label(form_frame, text="LOGIN", bg="#102A43", fg="white",
#          font=("Arial", 20, "bold")).place(x=170, y=120)

# # --- Input Fields ---
# tk.Label(form_frame, text="Email", bg="#102A43", fg="white",
#          font=("Arial", 12)).place(x=80, y=200)
# email_entry = tk.Entry(form_frame, width=35, font=("Arial", 11))
# email_entry.place(x=80, y=225)

# tk.Label(form_frame, text="Password", bg="#102A43", fg="white",
#          font=("Arial", 12)).place(x=80, y=265)
# password_entry = tk.Entry(form_frame, width=35, font=("Arial", 11), show="*")
# password_entry.place(x=80, y=290)

# # --- Login Button ---
# tk.Button(form_frame, text="LOGIN", bg="white", fg="#102A43",
#           font=("Arial", 11, "bold"), width=15, command=verify_login).place(x=170, y=350)

# # --- Register Navigation Link ---
# tk.Label(form_frame, text="Don't have an account?", bg="#102A43", fg="white",
#          font=("Arial", 9)).place(x=100, y=400)

# tk.Button(form_frame, text="Register", bg="#102A43", fg="lightblue",
#           font=("Arial", 9, "underline"), bd=0, cursor="hand2",
#           command=open_register).place(x=230, y=400)

# # --- Admin Access Link ---
# tk.Button(form_frame, text="Admin? Go to Admin Page", bg="#102A43", fg="lightblue",
#           font=("Arial", 9, "underline"), bd=0, cursor="hand2",
#           command=lambda: subprocess.Popen(["python", "admin.py"])).place(x=150, y=450)

# root.mainloop()



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import sqlite3
# import subprocess

# # ============= Database Helper =============
# def connect_db():
#     conn = sqlite3.connect("hotel_system.db")
#     return conn

# # ============= Login Window =============
# def login_window():
#     def login_user():
#         email = entry_email.get().strip()
#         password = entry_password.get().strip()

#         if not email or not password:
#             messagebox.showerror("Error", "All fields are required!")
#             return

#         conn = connect_db()
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
#         row = cur.fetchone()
#         conn.close()

#         if row:
#             messagebox.showinfo("Success", "Login successful!")
#             win.destroy()
#             subprocess.Popen(["python", "home.py"])  # <-- Opens Home page after login
#         else:
#             messagebox.showerror("Error", "Invalid email or password!")

#     def open_register():
#         win.destroy()
#         subprocess.Popen(["python", "register.py"])

#     win = tk.Tk()
#     win.title("Login - Hotel Management System")
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

#     # --- Login Form Frame ---
#     form_frame = tk.Frame(win, bg="white", bd=2, relief="ridge")
#     form_frame.place(x=320, y=160, width=300, height=300)

#     tk.Label(form_frame, text="LOGIN", bg="white", fg="#102A43", font=("Arial", 18, "bold")).place(x=105, y=25)

#     tk.Label(form_frame, text="Email:", bg="white", fg="black", font=("Arial", 11)).place(x=30, y=90)
#     entry_email = tk.Entry(form_frame, font=("Arial", 11), bd=1, relief="solid")
#     entry_email.place(x=30, y=115, width=240)

#     tk.Label(form_frame, text="Password:", bg="white", fg="black", font=("Arial", 11)).place(x=30, y=155)
#     entry_password = tk.Entry(form_frame, font=("Arial", 11), bd=1, relief="solid", show="*")
#     entry_password.place(x=30, y=180, width=240)

#     tk.Button(form_frame, text="Login", bg="#102A43", fg="white", font=("Arial", 11, "bold"),
#               command=login_user).place(x=95, y=220, width=100, height=30)

#     tk.Label(form_frame, text="Don’t have an account?", bg="white", fg="black", font=("Arial", 9)).place(x=60, y=260)
#     tk.Button(form_frame, text="Register", bg="#102A43", fg="lightblue", font=("Arial", 9, "underline"),
#               bd=0, cursor="hand2", command=open_register).place(x=210, y=260)

#     win.mainloop()

# if __name__ == "__main__":
#     login_window()



















############################################################################################



# import tkinter as tk
# from tkinter import messagebox
# import sqlite3
# import subprocess

# def open_register():
#     root.destroy()
#     subprocess.Popen(["python", "register.py"])

# def login_user():
#     email = entry_email.get()
#     password = entry_pass.get()

#     if not email or not password:
#         messagebox.showerror("Error", "All fields are required!")
#         return

#     conn = sqlite3.connect("hotel_system.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
#     row = cur.fetchone()
#     conn.close()

#     if row:
#         messagebox.showinfo("Login Successful", f"Welcome {row[1]}!")
#         root.destroy()
#         subprocess.Popen(["python", "home.py"])
#     else:
#         messagebox.showerror("Error", "Invalid email or password!")

# # -------- UI --------
# root = tk.Tk()
# root.title("Login")
# root.geometry("500x550")
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

# tk.Label(root, text="Welcome Back", font=("Arial", 20, "bold"), bg="#EAF0F1", fg="#0A2647").pack(pady=5)

# frame = tk.Frame(root, bg="#EAF0F1")
# frame.pack(pady=20)

# tk.Label(frame, text="Email", bg="#EAF0F1", fg="#0A2647", font=("Arial", 11, "bold")).grid(row=0, column=0, sticky="w")
# entry_email = tk.Entry(frame, width=35, font=("Arial", 11))
# entry_email.grid(row=1, column=0, pady=5)

# tk.Label(frame, text="Password", bg="#EAF0F1", fg="#0A2647", font=("Arial", 11, "bold")).grid(row=2, column=0, sticky="w", pady=(15,0))
# entry_pass = tk.Entry(frame, width=35, font=("Arial", 11), show="*")
# entry_pass.grid(row=3, column=0, pady=5)

# tk.Button(root, text="Login", width=20, bg="#0A2647", fg="white", font=("Arial", 11, "bold"),
#           command=login_user).pack(pady=15)

# tk.Button(root, text="New user? Register here", bg="#EAF0F1", fg="#144272",
#           font=("Arial", 10, "underline"), bd=0, command=open_register).pack()

# root.mainloop()





##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import subprocess

# --- Login Window ---
def open_login():
    root = tk.Tk()
    root.title("Rosemount Residencies - Login")
    root.geometry("900x600")
    root.configure(bg="white")
    root.resizable(False, False)

    def go_to_register():
        root.destroy()
        subprocess.Popen(["python", "register.py"])

    def login_user():
        email = entry_email.get().strip()
        password = entry_pass.get().strip()

        if not email or not password:
            messagebox.showwarning("Input Error", "Please fill all fields!")
            return

        try:
            conn = sqlite3.connect("hotel_system.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email=? AND password=?",
                           (email, password))
            result = cursor.fetchone()
            conn.close()
            if result:
                messagebox.showinfo("Login Successful", f"Welcome, {result[1]}!")
                root.destroy()
                subprocess.Popen(["python", "home.py"])
            else:
                messagebox.showerror("Error", "Invalid email or password!")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    # --- Left Image ---
    img = Image.open("rmlogo1.png")
    img = img.resize((370, 450))
    photo = ImageTk.PhotoImage(img)
    img_label = tk.Label(root, image=photo, bg="white")
    img_label.place(x=80, y=50)

    # --- Right Frame ---
    frame = tk.Frame(root, bg="#0b2e33", width=370, height=451)
    frame.place(x=450, y=51)

    title = tk.Label(frame, text="LOGIN", fg="white", bg="#0b2e33",
                     font=("Arial", 18, "bold"))
    title.place(x=130, y=40)

    tk.Label(frame, text="Email", bg="#0b2e33", fg="white",
             font=("Arial", 10, "bold")).place(x=40, y=120)
    entry_email = tk.Entry(frame, width=30, font=("Arial", 10), bd=1, relief="solid")
    entry_email.place(x=40, y=140)

    tk.Label(frame, text="Password", bg="#0b2e33", fg="white",
             font=("Arial", 10, "bold")).place(x=40, y=190)
    entry_pass = tk.Entry(frame, width=30, show="*", font=("Arial", 10), bd=1, relief="solid")
    entry_pass.place(x=40, y=210)

    def on_hover(e):
        btn_login["bg"] = "#14464c"

    def on_leave(e):
        btn_login["bg"] = "white"

    btn_login = tk.Button(frame, text="ENTER", font=("Arial", 10, "bold"),
                          bg="white", fg="#0b2e33", width=20, height=1,
                          bd=0, relief="flat", command=login_user)
    btn_login.place(x=75, y=270)
    btn_login.bind("<Enter>", on_hover)
    btn_login.bind("<Leave>", on_leave)

    tk.Label(frame, text="New user?", bg="#0b2e33", fg="white",
             font=("Arial", 10)).place(x=90, y=320)
    tk.Button(frame, text="Register", bg="#0b2e33", fg="skyblue", bd=0,
              cursor="hand2", command=go_to_register).place(x=160, y=321)

    root.mainloop()


if __name__ == "__main__":
    open_login()

