###############################trial 2#################################################

import tkinter as tk
from tkinter import ttk, messagebox, Label
from PIL import Image, ImageTk
import sqlite3
import os
from datetime import datetime
import time
from session import get_user_email

# --- Try to use connect_db from your database module, otherwise fallback ---
try:
    from database import connect_db
except Exception:
    def connect_db():
        db_path = os.path.join(os.path.dirname(__file__), "hotel_system.db")
        return sqlite3.connect(db_path)


# ---------- CONFIG ----------
WINDOW_W, WINDOW_H = 1000, 750

# 🔹 All menu item → image file mapping
MENU_IMAGES = {
    # Existing items
    "Pasta": "pasta.png",
    "Pizza": "pizza.png",
    "Burger": "burger.png",
    "Sandwich": "sandwich.png",
    "Brownie": "brownie.png",
    "Coffee": "coffee.png",
    "Juice": "juice.png",

    # NEW FOOD
    "Fried Rice": "fried rice.jpg",
    "Butter Chicken": "butter chicken.jpg",
    "Chowmein": "chowmein.jpg",
    "Malai Kofta": "malai kofta.jpg",
    "Paneer Tikka": "paneer tikka.jpg",
    "Naan": "naan.jpg",

    # NEW SNACKS
    "French Fries": "fries.jpg",
    "Spring Roll": "spring roll.jpg",
    "Veg Momos": "veg momos.jpg",
    "Garlic Bread": "garlic bread.jpg",   # make sure you have this, otherwise placeholder will show

    # NEW DRINKS  (assumed names – rename your files if needed)
    "Masala Tea": "masala tea.jpeg",
    "Cold Coffee": "cold coffee.jpeg",
    "Lemon Soda": "lemon soda.jpeg",
    "Milkshake": "milkshake.jpeg",
}

# 🔹 Prices
MENU_PRICES = {
    # Existing items
    "Pasta": 200,
    "Pizza": 350,
    "Burger": 180,
    "Sandwich": 130,
    "Brownie": 60,
    "Coffee": 100,
    "Juice": 120,

    # NEW FOOD
    "Fried Rice": 220,
    "Butter Chicken": 320,
    "Chowmein": 180,
    "Malai Kofta": 260,
    "Paneer Tikka": 260,
    "Naan": 60,

    # NEW SNACKS
    "French Fries": 140,
    "Spring Roll": 160,
    "Veg Momos": 120,
    "Garlic Bread": 130,

    # NEW DRINKS
    "Masala Tea": 40,
    "Cold Coffee": 120,
    "Lemon Soda": 60,
    "Milkshake": 150,
}

# 🔹 Category mapping for filter buttons
ITEM_CATEGORY = {
    # Existing
    "Pasta": "Food",
    "Pizza": "Snacks",
    "Burger": "Snacks",
    "Sandwich": "Snacks",
    "Brownie": "Snacks",
    "Coffee": "Drinks",
    "Juice": "Drinks",

    # NEW FOOD
    "Fried Rice": "Food",
    "Butter Chicken": "Food",
    "Chowmein": "Food",
    "Malai Kofta": "Food",
    "Paneer Tikka": "Food",
    "Naan": "Food",

    # NEW SNACKS
    "French Fries": "Snacks",
    "Spring Roll": "Snacks",
    "Veg Momos": "Snacks",
    "Garlic Bread": "Snacks",

    # NEW DRINKS
    "Masala Tea": "Drinks",
    "Cold Coffee": "Drinks",
    "Lemon Soda": "Drinks",
    "Milkshake": "Drinks",
}

# 🔹 Put ALL first now
CATEGORIES = ["All", "Food", "Drinks", "Snacks"]

BACKGROUND_IMAGE = "roomservicebg.jpg"


# ---------- DB: ensure table exists ----------
def init_service_table():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS room_service (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT,
            customer_name TEXT,
            item TEXT,
            room_no TEXT,
            service_type TEXT DEFAULT 'Food Order',
            cost REAL,
            status TEXT DEFAULT 'Completed'
        )''')
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error initializing room_service table:", e)


# ---------- UI Helpers ----------
def load_image_safe(path, size):
    try:
        img = Image.open(path).convert("RGBA")
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None


# ---------- MAIN APP ----------
class RoomServiceApp:
    def __init__(self, root):
        self.root = root
        self.cart = []   # <-- create empty cart list

        self.root.title("Room Service — Hotel Booking System")
        self.root.geometry(f"{WINDOW_W}x{WINDOW_H}")
        self.root.resizable(False, False)

        # 🔹 Category + item storage
        self.current_category = "All"
        self.item_frames = {}
        self.menu_photos = {}
        self.category_buttons = {}

        # Background
        if os.path.exists(BACKGROUND_IMAGE):
            bg_img = load_image_safe(BACKGROUND_IMAGE, (WINDOW_W, WINDOW_H))
            if bg_img:
                bg_label = tk.Label(root, image=bg_img)
                bg_label.image = bg_img
                bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            else:
                root.configure(bg="#f3f7fb")
        else:
            root.configure(bg="#f3f7fb")

        # Top title bar
        title_frame = tk.Frame(root, bg="#0A2647")
        title_frame.place(x=0, y=0, relwidth=1, height=70)
        tk.Label(title_frame, text="     Room Service", bg="#0A2647", fg="white",
                 font=("Arial", 20, "bold")).pack(side="left", padx=20)
        self.time_label = tk.Label(title_frame, bg="#0A2647", fg="#cfe3ff", font=("Arial", 10))
        self.time_label.pack(side="right", padx=18)
        self.update_time()
        
        # ------------menu bar------------
        from menu_bar import add_menu
        add_menu(self.root)

        # Main container
        container = tk.Frame(root, bg="#ffffff", bd=0)
        container.place(relx=0.5, rely=0.52, anchor="center", width=920, height=590)

        # Left menu
        menu_frame = tk.Frame(container, bg="#ffffff")
        menu_frame.place(x=10, y=10, width=520, height=580)

        tk.Label(menu_frame, text="Menu", bg="#ffffff", fg="#003366",
                 font=("Arial", 16, "bold")).pack(anchor="w", padx=10, pady=(6, 4))

        # 🔹 Horizontal Category Filter (All | Food | Drinks | Snacks)
        cat_frame = tk.Frame(menu_frame, bg="#ffffff")
        cat_frame.pack(anchor="w", padx=10, pady=(0, 8))

        for cat in CATEGORIES:
            btn = tk.Button(
                cat_frame,
                text=cat,
                font=("Arial", 10, "bold"),
                relief="ridge",
                bd=1,
                padx=8,
                pady=2,
                bg="#f2f5ff" if cat == "All" else "#ffffff",
                fg="#003366"
            )
            btn.config(command=lambda c=cat: self.filter_category(c))
            btn.pack(side="left", padx=4)
            self.category_buttons[cat] = btn

        menu_canvas = tk.Canvas(menu_frame, bg="#ffffff", highlightthickness=0)
        menu_scroll = ttk.Scrollbar(menu_frame, orient="vertical", command=menu_canvas.yview)
        menu_inner = tk.Frame(menu_canvas, bg="#ffffff")

        menu_inner.bind("<Configure>", lambda e: menu_canvas.configure(scrollregion=menu_canvas.bbox("all")))
        menu_canvas.create_window((0, 0), window=menu_inner, anchor="nw")
        menu_canvas.configure(yscrollcommand=menu_scroll.set)

        menu_canvas.pack(side="left", fill="both", expand=True)
        menu_scroll.pack(side="right", fill="y")

        self.menu_inner = menu_inner  # store reference just in case

        # build all menu items from dicts
        for item_name, price in MENU_PRICES.items():
            self._add_menu_item(menu_inner, item_name, price)

        # ---------- Right summary (Scrollable) ----------
        summary_outer = tk.Frame(container, bg="#f7fbff")
        summary_outer.place(x=540, y=10, width=370, height=580)

        # --- Create scrollable frame inside ---
        canvas = tk.Canvas(summary_outer, bg="#f7fbff", highlightthickness=0)
        scrollbar = ttk.Scrollbar(summary_outer, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f7fbff")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # ---------- Content inside scrollable frame ----------
        tk.Label(scrollable_frame, text="Order Summary", bg="#f7fbff", fg="#003366",
                 font=("Arial", 16, "bold")).pack(anchor="w", padx=12, pady=(6, 8))

        cols = ("Item", "Qty", "Price")
        self.cart_tree = ttk.Treeview(scrollable_frame, columns=cols, show="headings", height=10)
        for c in cols:
            self.cart_tree.heading(c, text=c)
            self.cart_tree.column(c, width=100, anchor="center")
        self.cart_tree.pack(padx=10, pady=6, fill="x")

        ctrl_frame = tk.Frame(scrollable_frame, bg="#f7fbff")
        ctrl_frame.pack(pady=8)
        ttk.Button(ctrl_frame, text="Remove Selected", command=self.remove_selected).grid(row=0, column=0, padx=6)
        ttk.Button(ctrl_frame, text="Clear Cart", command=self.clear_cart).grid(row=0, column=1, padx=6)

        self.total_var = tk.StringVar(value="Total: ₹0")
        tk.Label(scrollable_frame, textvariable=self.total_var, bg="#f7fbff", fg="#004080",
                 font=("Arial", 14, "bold")).pack(pady=6)

        # ---------- Customer + Room ----------
        tk.Label(scrollable_frame, text="Customer Name:", bg="#f7fbff").pack(anchor="w", padx=12, pady=(8, 0))
        self.entry_name = tk.Entry(scrollable_frame, width=28, font=("Arial", 11))
        self.entry_name.pack(padx=12, pady=6)

        tk.Label(scrollable_frame, text="Room Type:", bg="#f7fbff").pack(anchor="w", padx=12, pady=(8, 0))
        self.entry_room = tk.Entry(scrollable_frame, width=28, font=("Arial", 11))
        self.entry_room.pack(padx=12, pady=6)

        # Auto-fill from latest booking
        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("SELECT room_type FROM bookings ORDER BY id DESC LIMIT 1")
            result = cur.fetchone()
            conn.close()
            if result and result[0]:
                self.entry_room.insert(0, result[0])
                self.entry_room.config(state="readonly")
            else:
                self.entry_room.insert(0, "Not Assigned")
        except Exception as e:
            print("⚠️ Could not fetch room type:", e)
            self.entry_room.insert(0, "Not Assigned")

        # ---------- Action Buttons ----------
        action_frame = tk.Frame(scrollable_frame, bg="#f7fbff")
        action_frame.pack(pady=15, anchor="center")

        ttk.Button(action_frame, text="Confirm Order 💳", width=15, command=self.confirm_order).grid(row=0, column=0, padx=8, pady=5)
        ttk.Button(action_frame, text="Back to Home ⬅️", width=17, command=self.back_to_home).grid(row=0, column=1, padx=8, pady=5)

        # ---------- Toast Label (with fade-in animation) ----------
        self.toast = tk.Label(scrollable_frame, text="", bg="#f7fbff", fg="#008000", font=("Arial", 10, "bold"))
        self.toast.pack(pady=6)

        # 🔹 Live Order Preview (images of selected items)
        tk.Label(scrollable_frame, text="Live Order Preview", bg="#f7fbff", fg="#003366",
                 font=("Arial", 13, "bold")).pack(anchor="w", padx=12, pady=(4, 2))

        self.preview_frame = tk.Frame(scrollable_frame, bg="#e7f1ff")
        self.preview_frame.pack(fill="both", expand=False, padx=12, pady=(2, 10))

        # Optional: Enable mousewheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # ---------- Time Updater ----------
    def update_time(self):
        current_time = time.strftime("%d-%b-%Y %H:%M:%S")
        self.time_label.config(text=current_time)
        self.after_job = self.root.after(1000, self.update_time)

    # ---------- Cancel All Tkinter after() Jobs ----------
    def cancel_all_after_jobs(self):
        """Safely cancel all Tkinter .after jobs to avoid 'invalid command name' errors."""
        try:
            if hasattr(self, "after_job"):
                try:
                    self.root.after_cancel(self.after_job)
                except Exception:
                    pass
        except Exception:
            pass
        try:
            if hasattr(self.toast, "after_id"):
                try:
                    self.root.after_cancel(self.toast.after_id)
                except Exception:
                    pass
        except Exception:
            pass

        # 🔹 Cancel any remaining pending after() callbacks
        try:
            raw = self.root.tk.call('after', 'info')
            if raw:
                if isinstance(raw, str):
                    after_ids = raw.split()
                else:
                    after_ids = list(raw)
                for aid in after_ids:
                    try:
                        self.root.after_cancel(aid)
                    except Exception:
                        pass
        except Exception:
            pass

    # ---------- Menu Item Builder ----------
    def _add_menu_item(self, parent, item_name, price):
        frame = tk.Frame(parent, bg="#ffffff", bd=0)
        frame.pack(fill="x", pady=8, padx=10)

        # store frame for category filtering
        self.item_frames[item_name] = frame

        photo = None
        img_file = MENU_IMAGES.get(item_name)
        if img_file and os.path.exists(img_file):
            photo = load_image_safe(img_file, (110, 80))
        else:
            for ext in ("png", "jpg", "jpeg"):
                trial = f"{item_name.lower()}.{ext}"
                if os.path.exists(trial):
                    photo = load_image_safe(trial, (110, 80))
                    break

        if not photo:
            from PIL import Image
            placeholder = ImageTk.PhotoImage(Image.new("RGBA", (110, 80), (230, 230, 240)))
            photo = placeholder

        self.menu_photos[item_name] = photo
        img_lbl = tk.Label(frame, image=photo, bg="#ffffff")
        img_lbl.image = photo
        img_lbl.pack(side="left", padx=(0, 10))

        mid = tk.Frame(frame, bg="#ffffff")
        mid.pack(side="left", fill="both", expand=True)
        tk.Label(mid, text=item_name, font=("Arial", 13, "bold"), bg="#ffffff", fg="#003366").pack(anchor="w")
        tk.Label(mid, text=f"Price: ₹{price}", font=("Arial", 11), bg="#ffffff", fg="#444").pack(anchor="w", pady=(4, 0))

        # 🔹 Static Star Ratings (visual only)
        tk.Label(mid, text="⭐ ⭐ ⭐ ⭐ ⭐", font=("Arial", 10), bg="#ffffff", fg="#ffb300").pack(anchor="w", pady=(2, 0))

        right = tk.Frame(frame, bg="#ffffff")
        right.pack(side="right", padx=4)

        qty_var = tk.IntVar(value=1)
        tk.Button(right, text="-", width=2, command=lambda v=qty_var: v.set(max(1, v.get() - 1))).pack(side="left", padx=2)
        tk.Entry(right, width=3, justify="center", textvariable=qty_var).pack(side="left")
        tk.Button(right, text="+", width=2, command=lambda v=qty_var: v.set(v.get() + 1)).pack(side="left", padx=2)
        tk.Button(right, text="Add", bg="#0073e6", fg="white",
                  command=lambda n=item_name, q=qty_var, p=price: self.add_to_cart(n, q.get(), p)).pack(side="left", padx=(8, 0))

    # ---------- Category Filter ----------
    def filter_category(self, category):
        self.current_category = category

        # update button styles
        for cat, btn in self.category_buttons.items():
            if cat == category:
                btn.config(bg="#f2f5ff")
            else:
                btn.config(bg="#ffffff")

        # hide all frames
        for frame in self.item_frames.values():
            frame.pack_forget()

        # determine which items to show
        if category == "All":
            items = list(MENU_PRICES.keys())
        else:
            items = [it for it, cat in ITEM_CATEGORY.items() if cat == category]

        # re-pack frames in order
        for it in items:
            frame = self.item_frames.get(it)
            if frame is not None:
                frame.pack(fill="x", pady=8, padx=10)

    # ---------- Cart Operations ----------
    def add_to_cart(self, item, qty, price):
        for i, (it, q, u) in enumerate(self.cart):
            if it == item:
                self.cart[i] = (it, q + qty, u)
                self._refresh_cart_tree()
                self.show_toast(f"Updated {item} ×{qty}")
                return
        self.cart.append((item, qty, price))
        self._refresh_cart_tree()
        self.show_toast(f"Added {item} ×{qty}")

    def _refresh_cart_tree(self):
        for r in self.cart_tree.get_children():
            self.cart_tree.delete(r)
        total = 0
        for it, q, u in self.cart:
            self.cart_tree.insert("", "end", values=(it, q, f"₹{u * q}"))
            total += u * q
        self.total_var.set(f"Total: ₹{total}")

        # 🔹 Update live image preview
        self.update_preview()

    def remove_selected(self):
        sel = self.cart_tree.selection()
        if not sel:
            messagebox.showinfo("Select", "Select an item to remove.")
            return
        vals = self.cart_tree.item(sel[0], "values")
        item_name = vals[0]
        for i, (it, q, u) in enumerate(self.cart):
            if it == item_name:
                del self.cart[i]
                break
        self._refresh_cart_tree()

    def clear_cart(self):
        self.cart = []
        self._refresh_cart_tree()
        self.show_toast("Cart cleared")

    # ---------- Live Order Preview ----------
    def update_preview(self):
        # Clear previous previews
        for w in self.preview_frame.winfo_children():
            w.destroy()

        if not self.cart:
            tk.Label(self.preview_frame, text="No items added yet.",
                     bg="#e7f1ff", fg="#555", font=("Arial", 10, "italic")).pack(pady=8)
            return

        # Show up to 4 items visually
        max_items = 4
        for idx, (item, qty, price) in enumerate(self.cart[:max_items]):
            row_frame = tk.Frame(self.preview_frame, bg="#e7f1ff")
            row_frame.pack(fill="x", pady=5, padx=6)

            img = self.menu_photos.get(item)
            if img is not None:
                img_lbl = tk.Label(row_frame, image=img, bg="#e7f1ff")
                img_lbl.image = img
                img_lbl.pack(side="left", padx=(0, 8))

            txt = tk.Label(
                row_frame,
                text=f"{item}  x{qty}",
                bg="#e7f1ff",
                fg="#003366",
                font=("Arial", 11, "bold")
            )
            txt.pack(side="left", anchor="w")

    # ---------- Save & Navigation ----------
    def confirm_order(self):
        if not self.cart:
            messagebox.showwarning("Empty", "Cart is empty.")
            return

        name = self.entry_name.get().strip()
        if not name:
            messagebox.showwarning("Missing", "Enter customer name before confirming.")
            return

        room_no = self.entry_room.get().strip()
        if not room_no:
            messagebox.showwarning("Missing", "Room number is missing! Please enter or check bookings.")
            return

        # --- Show summary first ---
        summary_lines = [f"{it} x{q} = ₹{u * q}" for it, q, u in self.cart]
        summary = "\n".join(summary_lines)
        total = sum(u * q for it, q, u in self.cart)

        messagebox.showinfo(
            "Order Confirmed",
            f"Order for {room_no} confirmed.\n\n{summary}\n\nTotal: ₹{total}"
        )

        # --- Auto save order to DB as ONE ROW and go to payment ---
        try:
            conn = connect_db()
            cur = conn.cursor()

            from session import get_user_email
            user_email = get_user_email()

            # ✅ combine all items into a single string
            items_str = ", ".join([f"{it} x{q}" for it, q, u in self.cart])

            # ✅ total cost for the whole order
            total_cost = total

            # ✅ ONE insert only – one row per order
            cur.execute("""
                INSERT INTO room_service (user_email, customer_name, item, room_no, service_type, status, cost)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (user_email, name, items_str, room_no, "Food Order", "Completed", total_cost))

            conn.commit()
            conn.close()

            self.show_toast("Order saved and proceeding to payment 💳")
            self.clear_cart()
            self.entry_name.delete(0, tk.END)

            # ✅ Stop timers safely before switching windows
            self.cancel_all_after_jobs()

            # ✅ Automatically open Payment window
            try:
                self.root.destroy()
                import importlib.util
                current_folder = os.path.dirname(os.path.abspath(__file__))
                payment_path = os.path.join(current_folder, "payment.py")
                spec = importlib.util.spec_from_file_location("payment", payment_path)
                payment_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(payment_module)
            except Exception as e:
                messagebox.showerror("Error", f"Could not open Payment page: {e}")

        except Exception as e:
            messagebox.showerror("DB Error", f"Could not save order: {e}")

    def back_to_home(self):
        try:
            self.cancel_all_after_jobs()
        except Exception:
            pass
        try:
            self.root.destroy()
            __import__("home")
        except Exception:
            self.root.destroy()

    # ---------- Toast with simple fade-in effect ----------
    def show_toast(self, text, duration=2200):
        self.toast.config(text=text)

        # cancel previous clear if exists
        if hasattr(self.toast, "after_id"):
            try:
                self.root.after_cancel(self.toast.after_id)
            except Exception:
                pass

        # simple fade-in effect using gradual color change
        colors = ["#d9f9d9", "#b6f2b6", "#8bea8b", "#5fe35f", "#33db33", "#008000"]
        for i, col in enumerate(colors):
            self.root.after(i * 80, lambda c=col: self.toast.config(fg=c))

        # clear text after duration
        self.toast.after_id = self.root.after(duration, lambda: self.toast.config(text=""))


# ---------- Run ----------
if __name__ == "__main__":
    init_service_table()
    root = tk.Tk()
    app = RoomServiceApp(root)
    root.mainloop()
