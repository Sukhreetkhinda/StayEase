
import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import ttk
import subprocess

def open_main_app():
    root.destroy()  # close welcome window
    subprocess.run(["python", "projectfile_rs.py"])  # run your main file


# ---------- CONFIGURATION ----------
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 750
IMAGE_FILE = "blurredwlcmpage.JPG"

# ---------- FUNCTION TO OPEN NEW WINDOWS ----------
def open_window(title, message):
    new_win = tk.Toplevel(root)
    new_win.title(title)
    new_win.geometry("500x400")

    tk.Label(new_win, text=title, font=("Georgia", 20, "bold")).pack(pady=20)
    tk.Label(new_win, text=message, font=("Arial", 14)).pack(pady=10)
    tk.Button(new_win, text="Close", command=new_win.destroy).pack(pady=20)

# ---------- MENU BUTTON ACTIONS ----------
def open_home():
    open_window("Home", "Welcome to the Home Page!")

def open_pages():
    open_window("Pages", "Here are various pages...")

def open_rooms():
    open_window("Rooms", "View all rooms and options.")

def open_reservation():
    open_window("Reservation", "Make your reservations here.")

def open_blog():
    open_window("Blog", "Read our latest blog posts.")

# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Rosemount Residencies")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)

# ---------- BACKGROUND IMAGE ----------
bg_image = Image.open(IMAGE_FILE)
bg_image = bg_image.resize((WINDOW_WIDTH, WINDOW_HEIGHT))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# ---------- TOP BAR ----------
top_bar = tk.Canvas(root, bg="white", height=110, highlightthickness=0)
top_bar.place(x=0, y=0, width=WINDOW_WIDTH)

logo_image = Image.open("logo1.png")  # Replace with actual filename
logo_image = logo_image.resize((180, 125))  # Resize as needed
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(top_bar, image=logo_photo, bg="white", bd=0)
logo_label.image = logo_photo  # Keep a reference to prevent garbage collection
logo_label.place(x=10, y=0)  # Adjust x and y as needed


# ---------- BOTTOM BAR ----------
bottom_bar = tk.Canvas(root, bg="white", height=110, highlightthickness=0)
bottom_bar.place(x=0, y=638, width=WINDOW_WIDTH)

#------------menu bar------------
from menu_bar import add_menu
add_menu(root)

# ---------- INDIVIDUAL NAVIGATION BUTTONS ----------
btn_font = ("Georgia", 8, "bold")

home_btn = tk.Button(top_bar, text="HOME", font=btn_font, bg="white", fg="#0b2f76",
                     activebackground="lightgray", bd=0, command=open_home)
home_btn.place(x=637, y=75)

pages_btn = tk.Button(top_bar, text="PAGES", font=btn_font, bg="white", fg="#0b2f76",
                      activebackground="lightgray", bd=0, command=open_pages)
pages_btn.place(x=692, y=75)

rooms_btn = tk.Button(top_bar, text="ROOMS", font=btn_font, bg="white", fg="#0b2f76",
                      activebackground="lightgray", bd=0, command=open_rooms)
rooms_btn.place(x=753, y=75)

reservation_btn = tk.Button(top_bar, text="RESERVATION", font=btn_font, bg="white", fg="#0b2f76",
                            activebackground="lightgray", bd=0, command=open_reservation)
reservation_btn.place(x=819, y=75)

blog_btn = tk.Button(top_bar, text="BLOG", font=btn_font, bg="white", fg="#0c2963",
                     activebackground="lightgray", bd=0, command=open_blog)
blog_btn.place(x=930, y=75)

# ---------- TEXT OVER BACKGROUND ----------
canvas.create_text(500, 230, text="WELCOME TO", font=("Georgia", 24), fill="white")
canvas.create_text(500, 260, text="___", font=("Georgia", 38, "bold"), fill="white")
canvas.create_text(500, 340, text="ROSEMOUNT RESIDENCIES", font=("Georgia", 38, "bold"), fill="white")
canvas.create_text(500, 430, text="CRAFTED FOR COMFORT, DELIVERED WITH CARE", font=("Georgia", 14), fill="white")

# ---------- BOTTOM TITLE AND BUTTON ----------
bottom_label = tk.Label(root, text="LET YOUR PERFECT STAY START TODAY.", font=("Georgia", 16, "bold"), bg="white")
bottom_label.place(relx=0.5, rely=0.9,anchor="center")

# view_button = tk.Button(root, text="View All Rooms", font=("Georgia", 12), bg="#2f4f4f", fg="white",
#                         command=open_rooms)
# view_button.place(relx=0.5, rely=0.96, anchor="center")

from tkinter import ttk

# --- Style for Rounded Button ---
style = ttk.Style()
style.configure("Rounded.TButton",
                font=("Georgia", 12),
                padding=10,
                foreground="green",
                background="#0c2963",
                borderwidth=0,
                relief="flat")
style.map("Rounded.TButton",
          background=[("active", "#0c2963")])

# --- Create Rounded Button on Bottom Bar ---
get_started_btn = ttk.Button(root, text="Get Started", style="Rounded.TButton", command=open_main_app)
get_started_btn.place(relx=0.5, rely=0.96, anchor="center")



# ---------- RUN ----------
root.mainloop()

