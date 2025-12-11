# menu_bar.py
import tkinter as tk
import subprocess

def add_menu(window):
    # Frame for top-left menu (doesn't disturb existing layout)
    menu_frame = tk.Frame(window, bg="#e6f2ff")
    menu_frame.place(x=10, y=10)

    # Create Menu Button
    menu_button = tk.Menubutton(menu_frame, text="☰", font=("Arial", 11, "bold"),
                                bg="#0073e6", fg="white", activebackground="#005bb5",
                                cursor="hand2", relief="raised")
    menu_button.pack()

    # Dropdown Menu
    menu = tk.Menu(menu_button, tearoff=0, bg="white", fg="black", font=("Arial", 10))

    # Define navigation actions
    def open_page(file_name):
        try:
            window.destroy()
            subprocess.Popen(["python", file_name])
        except Exception as e:
            print(f"⚠️ Could not open {file_name}: {e}")

    # Add menu options
    menu.add_command(label="Register / Login", command=lambda: open_page("projectfile_rs.py"))
    menu.add_command(label="Admin", command=lambda: open_page("admin.py"))
    menu.add_command(label="Home", command=lambda: open_page("home.py"))
    menu.add_command(label="Room Info", command=lambda: open_page("room_info.py"))
    menu.add_command(label="Room Service", command=lambda: open_page("room_service.py"))
    menu.add_command(label="Booking", command=lambda: open_page("booking.py"))
    menu.add_command(label="Payment", command=lambda: open_page("payment.py"))

    menu_button.config(menu=menu)
