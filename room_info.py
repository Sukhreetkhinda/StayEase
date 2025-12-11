################################trial finlll###############################


import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import importlib.util
import subprocess

# --- Function to open booking.py window ---
def open_booking_window():
    try:
        current_folder = os.path.dirname(os.path.abspath(__file__))
        booking_path = os.path.join(current_folder, "booking.py")
        spec = importlib.util.spec_from_file_location("booking", booking_path)
        booking_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(booking_module)
    except Exception as e:
        messagebox.showerror("Error", f"Cannot open booking page: {e}")

# --- Function triggered by BOOK NOW ---
def book_now(room_type):
    messagebox.showinfo("Booking", f"You selected the {room_type}. Redirecting to booking page...")
    try:
        # Close current Room Info window
        root.destroy()

        # ✅ Open booking.py directly using subprocess
        current_folder = os.path.dirname(os.path.abspath(__file__))
        booking_file = os.path.join(current_folder, "booking.py")
        subprocess.Popen(["python", booking_file])
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open Booking page:\n{e}")


# ---------- IMAGE SLIDER STATE ----------
room_sliders = {}  # {room_title: {"images": [...], "index": 0, "label": img_label}}

def init_image_slider(room_title, img_label, base_img_file):
    """
    Setup a simple auto image slider for each room.
    It will look for base_name1.jpg, base_name2.jpg... if they exist,
    otherwise it will just use the main image.
    """
    try:
        current_folder = os.path.dirname(os.path.abspath(__file__))
        base_name, ext = os.path.splitext(base_img_file)

        images = []

        # Look for numbered variants: single1.jpg, single2.jpg, etc.
        for i in range(1, 6):
            candidate = f"{base_name}{i}{ext}"
            path = os.path.join(current_folder, candidate)
            if os.path.exists(path):
                img = Image.open(path)
                img = img.resize((260, 160))
                images.append(ImageTk.PhotoImage(img))

        # Always include original image as fallback/first slide
        orig_path = os.path.join(current_folder, base_img_file)
        if os.path.exists(orig_path):
            img = Image.open(orig_path)
            img = img.resize((260, 160))
            images.insert(0, ImageTk.PhotoImage(img))

        if not images:
            return  # no images found, keep static

        room_sliders[room_title] = {"images": images, "index": 0, "label": img_label}

        # Set initial image from slider list
        img_label.config(image=images[0])
        img_label.image = images[0]

        # Start cycle if more than one image
        if len(images) > 1:
            def cycle():
                data = room_sliders.get(room_title)
                if not data:
                    return
                imgs = data["images"]
                if len(imgs) <= 1:
                    return
                data["index"] = (data["index"] + 1) % len(imgs)
                new_img = imgs[data["index"]]
                data["label"].config(image=new_img)
                data["label"].image = new_img
                img_label.after(2500, cycle)  # change every 2.5 sec

            img_label.after(2500, cycle)
    except Exception as e:
        print(f"⚠️ Error setting slider for {room_title}: {e}")


# --- Function to load room images ---
def load_image(img_file):
    try:
        current_folder = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(current_folder, img_file)
        img = Image.open(img_path)
        img = img.resize((260, 160))
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"⚠️ Error loading image {img_file}: {e}")
        return None


# --- Room-wise amenities (different for each room) ---
AMENITIES_BY_ROOM = {
    "Single Room": [
        ("📶", "Free high-speed WiFi"),
        ("❄️", "Air Conditioning"),
        ("📺", "LED TV"),
        ("🍳", "Complimentary Breakfast"),
        ("🛏️", "Cozy Single Bed"),
        ("🧹", "Daily Housekeeping"),
    ],
    "Double Room": [
        ("📶", "Free high-speed WiFi"),
        ("❄️", "Air Conditioning"),
        ("📺", "Smart TV"),
        ("🍳", "Breakfast Included"),
        ("🛏️", "Comfortable Double Bed"),
        ("🧹", "Daily Housekeeping"),
    ],
    "Deluxe Room": [
        ("📶", "Free high-speed WiFi"),
        ("❄️", "Air Conditioning"),
        ("📺", "LED TV"),
        ("🍳", "Breakfast & Dinner Included"),   # ✅ dinner
        ("🥤", "Mini Bar"),
        ("🛏️", "Premium King Bed"),
        ("🧹", "Daily Housekeeping"),
        ("🛎️", "24/7 Room Service"),
    ],
    "Suite": [
        ("📶", "Free high-speed WiFi"),
        ("❄️", "Air Conditioning"),
        ("📺", "Smart TV"),
        ("🍳", "Breakfast & Dinner Included"),   # ✅ dinner
        ("🛁", "Jacuzzi"),
        ("🌅", "Private Balcony View"),
        ("🛏️", "Luxury King Bed"),
        ("🛎️", "Personalized Butler Service"),
        ("🧹", "Daily Housekeeping"),
    ],
}


# --- Static reviews for rooms ---
ROOM_RATINGS = {
    "Single Room": "⭐ ⭐ ⭐",
    "Double Room": "⭐ ⭐ ⭐ ⭐ ",
    "Deluxe Room": "⭐ ⭐ ⭐ ⭐ ⭐",
    "Suite": "⭐ ⭐ ⭐ ⭐ ⭐"
}



# --- Amenities popup (systematic grid) ---
def open_amenities_popup(room_type):
    popup = tk.Toplevel(root)
    popup.title(f"{room_type} – Amenities")
    popup.geometry("420x360")
    popup.config(bg="#f5f8ff")

    tk.Label(
        popup,
        text=f"Amenities for {room_type}",
        font=("Arial", 14, "bold"),
        bg="#f5f8ff",
        fg="#003366"
    ).grid(row=0, column=0, columnspan=2, pady=10)

    amenities = AMENITIES_BY_ROOM.get(room_type, AMENITIES_BY_ROOM["Single Room"])

    start_row = 1
    for i, (icon, text) in enumerate(amenities):
        r = start_row + i
        tk.Label(
            popup,
            text=icon,
            font=("Arial", 14),
            bg="#f5f8ff"
        ).grid(row=r, column=0, padx=(25, 8), pady=3, sticky="w")

        tk.Label(
            popup,
            text=text,
            font=("Arial", 11),
            bg="#f5f8ff",
            anchor="w",
            justify="left"
        ).grid(row=r, column=1, pady=3, sticky="w")

    tk.Button(
        popup,
        text="Close",
        font=("Arial", 10, "bold"),
        bg="#0073e6",
        fg="white",
        activebackground="#005bb5",
        cursor="hand2",
        command=popup.destroy
    ).grid(row=start_row + len(amenities), column=0, columnspan=2, pady=12)


# --- Main window setup ---
root = tk.Tk()
root.title("Room Information")
root.geometry("1000x750")


# --- Load background image ---
try:
    bg_image = Image.open("roominfo.jpg")  # Background image in same folder
    bg_image = bg_image.resize((1000, 750))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    print("⚠️ Background image not found — using default color.")
    root.config(bg="#e6f2ff")

# --- Heading text ---
heading = tk.Label(root, text="✨ Luxury Rooms ✨", font=("Arial", 24, "bold"),
                   bg="#e6f2ff", fg="#003366")
heading.place(x=350, y=20)

# --- Scrollable frame setup ---
canvas = tk.Canvas(root, bg="#e6f2ff", highlightthickness=0)
scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
frame = tk.Frame(canvas, bg="#e6f2ff")

#------------menu bar------------
from menu_bar import add_menu
add_menu(root)

rooms = [
    (
        "Single Room",
        "A cozy room for one person. Ideal for solo travelers.",
        "single.jpg",
        "₹1500 / night",
        "• Free WiFi  • Air Conditioning  • Breakfast Included"
    ),
    (
        "Double Room",
        "Perfect for two guests. Comes with all modern amenities.",
        "double.jpg",
        "₹2500 / night",
        "• Free WiFi  • Air Conditioning  • Breakfast Included  • Smart TV"
    ),
    (
        "Deluxe Room",
        "Spacious and comfortable room with premium facilities.",
        "deluxe.jpg",
        "₹4000 / night",
        "• Free WiFi  • Air Conditioning  • Breakfast & Dinner Included  • Mini Bar  • 24/7 Room Service"
    ),
    (
        "Suite",
        "Luxury suite with separate living area and scenic view.",
        "suite.jpg",
        "₹7000 / night",
        "• Free WiFi  • Air Conditioning  • Breakfast & Dinner Included  • Jacuzzi  • Balcony View  • Personalized Butler"
    ),
]

# --- Display room cards ---
for i, (title, desc, img_file, price, features) in enumerate(rooms):
    img_tk = load_image(img_file)
    room_frame = tk.Frame(frame, bg="#e6f2ff", bd=2, relief="groove")
    room_frame.grid(row=i, column=0, pady=20, padx=30, sticky="w")
    
    #---------------frame part-----------------
    # Image (with slider)
    if img_tk:
        img_label = tk.Label(room_frame, image=img_tk, bg="#bc9763")
        img_label.image = img_tk
        img_label.grid(row=0, column=0, rowspan=8, padx=15, pady=10)

        # 🔹 Initialize image slider for this room
        init_image_slider(title, img_label, img_file)

    # Room Info
    tk.Label(room_frame, text=title, font=("Arial", 14, "bold"),
             bg="#e6f2ff", fg="#003366").grid(row=0, column=1, sticky="w", pady=(10, 0))
    tk.Label(room_frame, text=desc, font=("Arial", 11),
             bg="#e6f2ff", wraplength=400, justify="left").grid(row=1, column=1, sticky="w", pady=2)

    # Price
    tk.Label(room_frame, text=f"Price: {price}", font=("Arial", 11, "bold"),
             bg="#e6f2ff", fg="#004080").grid(row=2, column=1, sticky="w", pady=2)

    # Amenities icons row (just visual icons line)
    amenities_icons = "📶 WiFi    ❄️ AC    📺 TV    🍳 Breakfast"
    tk.Label(
        room_frame,
        text=amenities_icons,
        font=("Arial", 11),
        bg="#e6f2ff",
        fg="#003366"
    ).grid(row=3, column=1, sticky="w", pady=2)


    

    # # Features text line
    # tk.Label(room_frame, text=f"Features: {features}", font=("Arial", 11),
    #          bg="#e6f2ff", wraplength=400, justify="left").grid(row=4, column=1, sticky="w", pady=2)

    # # Guest Reviews (static)
    # reviews = ROOM_REVIEWS.get(title, [])
    # if reviews:
    #     tk.Label(
    #         room_frame,
    #         text="Guest Reviews:",
    #         font=("Arial", 11, "bold"),
    #         bg="#e6f2ff",
    #         fg="#003366"
    #     ).grid(row=5, column=1, sticky="w", pady=(6, 2))

    #     for j, review_text in enumerate(reviews[:2]):  # show max 2
    #         tk.Label(
    #             room_frame,
    #             text=review_text,
    #             font=("Arial", 10),
    #             bg="#e6f2ff",
    #             wraplength=400,
    #             justify="left"
    #         ).grid(row=6 + j, column=1, sticky="w", pady=1)

    # Book Now Button
    tk.Button(room_frame, text="BOOK NOW", font=("Arial", 10, "bold"),
              bg="#0073e6", fg="white", activebackground="#005bb5",
              cursor="hand2", command=lambda t=title: book_now(t)).grid(row=0, column=2, padx=20, pady=10)

    # View Amenities Button
    tk.Button(
        room_frame,
        text="View Amenities",
        font=("Arial", 9, "bold"),
        bg="#ffffff",
        fg="#0073e6",
        activebackground="#e0f0ff",
        cursor="hand2",
        bd=1,
        relief="ridge",
        command=lambda t=title: open_amenities_popup(t)
    ).grid(row=1, column=2, padx=20, sticky="n")


# --- Configure scrolling ---
canvas.create_window((0, 0), window=frame, anchor='nw')
canvas.update_idletasks()
canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
canvas.place(x=60, y=80, width=860, height=640)
scroll_y.place(x=930, y=80, height=640)

# --- Run main window ---
root.mainloop()

