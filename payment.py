
#########################finallll###################################################

import tkinter as tk
from tkinter import messagebox
import sqlite3
from database import connect_db
from session import get_user_email

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors  # for simple colors

import tempfile
import datetime
import os
import threading  # background work

from email_config import SENDER_EMAIL, SENDER_PASSWORD


# # --------------------------------------
# # Email Config  (KEEP YOUR REAL PASSWORD LOCALLY)
# # --------------------------------------
# SENDER_EMAIL = "khindasukhreet@gmail.com"          # your Gmail
# SENDER_PASSWORD = "lybk nuor gjyr ywtc"  # Gmail APP password


# ========== DATABASE TOTAL CALCULATION ==========
def calculate_total():
    conn = connect_db()
    cursor = conn.cursor()

    # Booking total (uses total_cost column)
    try:
        cursor.execute("SELECT SUM(total_cost) FROM bookings")
        booking_total = cursor.fetchone()[0] or 0
    except Exception:
        booking_total = 0

    # Room service total (uses cost column)
    try:
        cursor.execute("SELECT SUM(cost) FROM room_service")
        service_total = cursor.fetchone()[0] or 0
    except Exception:
        service_total = 0

    conn.close()
    return booking_total + service_total


# ========== RECORD PAYMENT ==========
def record_payment(amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT,
            amount REAL,
            method TEXT,
            payment_date TEXT,
            status TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO payments (user_email, amount, method, payment_date, status)
        VALUES (?, ?, ?, ?, ?)
    """, (
        get_user_email(),  # logged-in user email
        amount,            # total amount paid
        "Online",          # payment method
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # payment date
        "Completed"        # status
    ))

    conn.commit()
    conn.close()


# ========== SIMPLE, FORMATTED RECEIPT PDF ==========
def generate_receipt_pdf(
    amount,
    check_in,
    check_out,
    days,
    room_type,
    guest_name,
    guests=1,
    rooms=1,
    booking_id=None,
    show_message=True
):
    """
    Simpler + faster PDF:
    - Still formatted
    - Uses receipt.jpg as full background if available
    """

    try:
        # Basic tax math (simple)
        tax_amount = round(amount * 0.05, 2)
        subtotal = round(amount - tax_amount, 2)

        # File path
        filename = f"receipt_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        file_path = os.path.join(tempfile.gettempdir(), filename)

        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter

        # --------- FULL BACKGROUND IMAGE (receipt.jpg) ----------
        bg_path = os.path.join(os.path.dirname(__file__), "receipt.jpg")
        if os.path.exists(bg_path):
            try:
                c.drawImage(
                    bg_path,
                    0,
                    0,
                    width=width,
                    height=height,
                    preserveAspectRatio=False,
                    mask="auto"
                )
            except Exception:
                c.setFillColorRGB(0.96, 0.96, 0.96)
                c.rect(0, 0, width, height, fill=1, stroke=0)
        else:
            c.setFillColorRGB(0.96, 0.96, 0.96)
            c.rect(0, 0, width, height, fill=1, stroke=0)

        # Simple white card in center
        margin = 50
        card_width = width - 2 * margin
        card_height = height - 2 * margin
        c.setFillColor(colors.white)
        c.roundRect(margin, margin, card_width, card_height, 10, fill=1, stroke=0)

        # --------- Logo + Hotel name ----------
        hotel_name = "Rosemount Residencies"
        logo_x = margin + 20
        logo_y = height - margin - 60
        logo_size = 45

        logo_path = os.path.join(os.path.dirname(__file__), "rmlogo1.png")
        if os.path.exists(logo_path):
            try:
                c.drawImage(
                    logo_path,
                    logo_x,
                    logo_y,
                    width=logo_size,
                    height=logo_size,
                    preserveAspectRatio=True,
                    mask="auto",
                )
            except Exception:
                pass

        c.setFillColor(colors.HexColor("#003366"))
        c.setFont("Helvetica-Bold", 18)
        c.drawString(logo_x + logo_size + 12, logo_y + 20, hotel_name)

        # Heading
        y = height - margin - 100
        display_name = guest_name or "Guest"
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 20)
        c.drawString(margin + 20, y, f"Payment Receipt")

        y -= 18
        c.setFont("Helvetica", 11)
        c.drawString(margin + 20, y, f"Guest: {display_name}")

        y -= 16
        if booking_id is None:
            booking_id = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        c.drawString(margin + 20, y, f"Confirmation #: {booking_id}")

        # Divider
        y -= 18
        c.setStrokeColor(colors.HexColor("#cccccc"))
        c.line(margin + 20, y, margin + card_width - 20, y)

        # Stay details
        y -= 22
        c.setFont("Helvetica-Bold", 11)
        c.drawString(margin + 20, y, "Stay Details:")

        c.setFont("Helvetica", 11)
        y -= 18
        c.drawString(margin + 40, y, f"Room Type : {room_type or 'N/A'}")
        y -= 16
        c.drawString(margin + 40, y, f"Check-in  : {check_in}")
        y -= 16
        c.drawString(margin + 40, y, f"Check-out : {check_out}")
        y -= 16
        c.drawString(margin + 40, y, f"Nights    : {days}")
        y -= 16
        c.drawString(margin + 40, y, f"Guests    : {guests}")
        y -= 16
        c.drawString(margin + 40, y, f"Rooms     : {rooms}")

        # Divider
        y -= 20
        c.setStrokeColor(colors.HexColor("#cccccc"))
        c.line(margin + 20, y, margin + card_width - 20, y)

        # Amount summary
        y -= 22
        c.setFont("Helvetica-Bold", 11)
        c.drawString(margin + 20, y, "Payment Summary:")

        c.setFont("Helvetica", 11)
        y -= 18
        c.drawString(margin + 40, y, f"Subtotal (before GST): ₹{subtotal:.2f}")
        y -= 16
        c.drawString(margin + 40, y, f"GST (5%): ₹{tax_amount:.2f}")

        # Final total
        y -= 24
        c.setStrokeColor(colors.HexColor("#bbbbbb"))
        c.line(margin + 20, y, margin + card_width - 20, y)
        y -= 22

        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(colors.HexColor("#0073e6"))
        c.drawString(margin + 20, y, f"Total Amount Paid: ₹{amount:.2f}")
        c.setFillColor(colors.black)

        # Footer note
        y -= 40
        c.setFont("Helvetica-Oblique", 8)
        c.setFillColor(colors.HexColor("#555555"))
        c.drawString(margin + 20, y, "Thank you for choosing Rosemount Residencies.")
        y -= 12
        c.drawString(margin + 20, y, "Please keep this receipt for your records.")

        c.save()

        if show_message:
            messagebox.showinfo("PDF Saved", f"Receipt saved at:\n{file_path}")

        return file_path

    except Exception as e:
        messagebox.showerror("PDF Error", f"Failed to generate PDF: {e}")
        return None


# ========== EMAIL SENDER (no popup, raises on error if asked) ==========
def send_email(amount, recipient_email, pdf_path=None, show_popup=True):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg['Subject'] = "Hotel Payment Confirmation"

    body = f"""Dear Guest,

Your payment of ₹{amount} was successful.

Thank you for choosing our hotel!

Regards,
Rosemount Residencies
"""
    msg.attach(MIMEText(body, 'plain'))

    # Attach PDF receipt if available
    if pdf_path and os.path.exists(pdf_path):
        try:
            with open(pdf_path, "rb") as f:
                part = MIMEApplication(f.read(), _subtype="pdf")
            part.add_header(
                'Content-Disposition',
                'attachment',
                filename=os.path.basename(pdf_path)
            )
            msg.attach(part)
        except Exception as e:
            if show_popup:
                messagebox.showerror("Attachment Error", f"Could not attach receipt PDF: {e}")
            else:
                raise
            return

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        if show_popup:
            messagebox.showerror("Email Error", f"Failed to send email:\n{e}")
        else:
            raise


# ========== SUCCESS WINDOW (no download button) ==========
def show_success_window(amount, check_in, check_out, days, room_type, guest_name, recipient_email):
    success = tk.Toplevel(window)
    success.title("Payment Successful")
    success.geometry("420x340")
    success.config(bg="#d4edda")

    tk.Label(
        success,
        text="✅ Payment Successful!",
        font=("Arial", 18, "bold"),
        bg="#d4edda",
        fg="#155724"
    ).pack(pady=15)

    tk.Label(
        success,
        text=f"Amount Paid: ₹{amount}",
        font=("Arial", 14),
        bg="#d4edda",
        fg="#155724"
    ).pack(pady=5)

    tk.Label(
        success,
        text=f"Receipt sent to:\n{recipient_email}",
        font=("Arial", 10),
        bg="#d4edda",
        fg="#155724",
        justify="center"
    ).pack(pady=5)

    tk.Button(
        success,
        text="Close",
        bg="#28a745", fg="white",
        font=("Arial", 11, "bold"),
        command=success.destroy
    ).pack(pady=20)


# ========== PAYMENT PROCESS (with PROCESSING BOX + email before success) ==========
def process_payment():
    amount = calculate_total()

    if amount == 0:
        messagebox.showerror("Error", "No billing amount available!")
        return

    tax = round(amount * 0.05, 2)
    grand_total = amount + tax

    # Record payment (quick)
    try:
        record_payment(grand_total)
    except Exception as e:
        messagebox.showerror("DB Error", f"Could not record payment: {e}")
        return

    # Fetch last booking (quick DB query)
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id, name, user_email, room_type, check_in, check_out, days, guests, rooms, total_cost
            FROM bookings
            ORDER BY id DESC LIMIT 1
        """)
        data = cursor.fetchone()
    except Exception:
        data = None
    conn.close()

    if data:
        booking_id, guest_name, user_email, room_type, check_in, check_out, days, guests, rooms, total_cost = data
        recipient_email = user_email or SENDER_EMAIL
    else:
        booking_id = None
        guest_name = "Guest"
        room_type = "N/A"
        check_in = "N/A"
        check_out = "N/A"
        days = 0
        guests = 1
        rooms = 1
        total_cost = amount
        recipient_email = SENDER_EMAIL

    # ---------- Show PROCESSING window ----------
    processing = tk.Toplevel(window)
    processing.title("Processing Payment")
    processing.geometry("320x140")
    processing.config(bg="#f0f4ff")
    processing.resizable(False, False)

    tk.Label(
        processing,
        text="Processing your payment...\nPlease wait.",
        font=("Arial", 11),
        bg="#f0f4ff",
        fg="#003366",
        justify="center"
    ).pack(pady=25)

    # Make it modal (user can't click main window)
    processing.transient(window)
    processing.grab_set()

    # Worker to do PDF + email in background
    def worker():
        error_message = None
        pdf_path = None

        try:
            pdf_path = generate_receipt_pdf(
                grand_total,
                check_in,
                check_out,
                days,
                room_type,
                guest_name,
                guests=guests,
                rooms=rooms,
                booking_id=booking_id,
                show_message=False
            )
        except Exception as e:
            error_message = f"Could not generate receipt PDF:\n{e}"

        if not error_message and recipient_email:
            try:
                send_email(grand_total, recipient_email, pdf_path, show_popup=False)
            except Exception as e:
                error_message = f"Failed to send email:\n{e}"

        # Back to main thread to update UI
        def finish():
            try:
                processing.destroy()
            except Exception:
                pass

            if error_message:
                messagebox.showerror("Payment Notice", error_message)
            else:
                # ✅ Only now show SUCCESS (after email+PDF done)
                show_success_window(grand_total, check_in, check_out, days, room_type, guest_name, recipient_email)

        window.after(0, finish)

    threading.Thread(target=worker, daemon=True).start()


# ========== MAIN WINDOW UI ==========
window = tk.Tk()
window.title("Payment - Hotel Booking System")
window.geometry("520x520")
window.config(bg="#e6f2ff")

from menu_bar import add_menu
add_menu(window)

tk.Label(
    window,
    text="💳 PAYMENT PORTAL",
    font=("Arial", 20, "bold"),
    bg="#e6f2ff",
    fg="#004080"
).pack(pady=20)

amount = calculate_total()
tax = round(amount * 0.05, 2)
grand_total = amount + tax

summary_frame = tk.Frame(window, bg="white", bd=2, relief="groove")
summary_frame.pack(pady=15, ipadx=10, ipady=10)

tk.Label(summary_frame, text=f"Subtotal: ₹{amount}", font=("Arial", 12), bg="white").pack()
tk.Label(summary_frame, text=f"GST (5%): ₹{tax}", font=("Arial", 12), bg="white").pack()
tk.Label(
    summary_frame,
    text=f"Grand Total: ₹{grand_total}",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="#0073e6"
).pack()

pay_button = tk.Button(
    window,
    text="Pay Now with Razorpay",
    bg="#0073e6", fg="white",
    width=25,
    command=process_payment
)
pay_button.pack(pady=20)

tk.Button(
    window,
    text="Back to Home",
    bg="#e6f2ff", fg="#004080",
    borderwidth=0,
    command=lambda: [window.destroy(), __import__('home')]
).pack(pady=15)

window.mainloop()
