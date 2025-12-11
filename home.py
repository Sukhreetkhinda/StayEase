
##########################3333333333333333333333333333333333333333333333333333333333333333333333333333333333

import tkinter as tk
import time
import subprocess
from PIL import Image, ImageTk

def open_home():
    root = tk.Tk()
    root.title("Hotel Home - Minimal Animated")
    root.geometry("900x700")
    root.resizable(False, False)
    
    # 1. SETUP CANVAS (Replaces Background Label)
    # This allows us to draw text and buttons directly on the image
    canvas = tk.Canvas(root, width=900, height=700, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # ===== Background Image =====
    # We keep a reference to the image (root.bg_photo) to prevent garbage collection
    try:
        bg_img = Image.open("homebg.jpg")   # Ensure this matches your file name
        bg_img = bg_img.resize((900, 700), Image.LANCZOS)
        root.bg_photo = ImageTk.PhotoImage(bg_img)
        # Draw image at 0,0
        canvas.create_image(0, 0, image=root.bg_photo, anchor="nw")
    except Exception as e:
        print(f"Image Error: {e}")
        canvas.configure(bg="#f4f4f4") # Fallback color

    # ===== Header Text (Transparent Background) =====
    # Using create_text instead of Label removes the white box background
    canvas.create_text(450, 60, text="Rosemount Residency", 
                       font=("Arial", 32, "bold"), fill="#FFFFFF")

    # Placeholder for typing animation text
    subtitle_id = canvas.create_text(450, 105, text="", 
                                     font=("Arial", 16, "italic"), fill="#FFFFFF")

    # ------------ Menu Bar ------------
    # We add this after the canvas so it floats on top
    try:
        from menu_bar import add_menu
        add_menu(root)
    except ImportError:
        pass

    # ===== Typing Animation Logic =====
    def type_text(text):
        # Reset text
        for i in range(len(text)):
            if not canvas.winfo_exists():
                return 
            # Update the text item on the canvas
            canvas.itemconfig(subtitle_id, text=text[:i])
            root.update()
            time.sleep(0.05)

    # ===== Function to open other pages (Logic Unchanged) =====
    def open_page(filename):
        root.destroy()
        subprocess.Popen(["python", filename])

    # ===== Custom Canvas Button Function =====
    def create_canvas_button(x, y, text, command):
        """Creates a custom button drawn on the canvas."""
        btn_w, btn_h = 250, 50
        
        # Coordinates for the rectangle
        x1, y1 = x - btn_w/2, y - btn_h/2
        x2, y2 = x + btn_w/2, y + btn_h/2

        # 1. Draw the Rectangle (The Button Body)
        # fill: Button color, outline: Border color
        rect_id = canvas.create_rectangle(x1, y1, x2, y2, 
                                          fill="#205295", outline="white", width=2)
        
        # 2. Draw the Text
        text_id = canvas.create_text(x, y, text=text, 
                                     font=("Arial", 14, "bold"), fill="white")

        # 3. Hover Effects
        def on_enter(e):
            canvas.itemconfig(rect_id, fill="#144272") # Darker blue on hover
            root.config(cursor="hand2") # Change cursor to hand

        def on_leave(e):
            canvas.itemconfig(rect_id, fill="#205295") # Original blue
            root.config(cursor="")

        # 4. Click Event
        def on_click(e):
            if command:
                command()
            else:
                root.destroy()

        # 5. Bind events to both the rectangle and the text
        for item in [rect_id, text_id]:
            canvas.tag_bind(item, "<Enter>", on_enter)
            canvas.tag_bind(item, "<Leave>", on_leave)
            canvas.tag_bind(item, "<Button-1>", on_click)

    # ===== Create The Buttons =====
    # We define the list exactly as before
    options = {
        "Room Info": "room_info.py",
        "Booking": "booking.py",
        "Room Service": "room_service.py",
        "Payment": "payment.py",
        "Exit": None
    }

    # Starting Y position for the first button
    start_y = 250
    spacing = 70

    for index, (text, file) in enumerate(options.items()):
        # Create the handler for this specific button
        def handler(f=file):
            if f:
                open_page(f)
            else:
                root.destroy()
        
        # Draw the button on the canvas
        create_canvas_button(450, start_y + (index * spacing), text, handler)

    # Start the typing animation
    type_text("Welcome! Choose an option below to continue...")

    root.mainloop()

if __name__ == "__main__":
    open_home()