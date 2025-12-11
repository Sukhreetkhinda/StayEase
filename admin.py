
####################################################################################

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

# ---------------- Database Connection ----------------
try:
    from database import connect_db
except Exception:
    def connect_db():
        p = os.path.join(os.path.dirname(__file__), "hotel_system.db")
        return sqlite3.connect(p)


# ---------------- Admin Dashboard ----------------
class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard - Hotel Management System")
        self.root.geometry("1000x600")
        self.root.config(bg="#0A2647")
        
        #------------menu bar------------
        from menu_bar import add_menu
        add_menu(self.root)

        tk.Label(self.root, text="Admin Dashboard", bg="#0A2647", fg="white",
                 font=("Arial", 20, "bold")).pack(pady=12)

        # Notebook for each table
        self.nb = ttk.Notebook(self.root)
        self.nb.pack(expand=1, fill="both", padx=10, pady=10)

        # Determine tables available in DB
        self.tables = self.get_table_list()
        self.trees = {}  # map table -> treeview

        for t in self.tables:
            frame = tk.Frame(self.nb, bg="#0A2647")
            self.nb.add(frame, text=t)
            tree = ttk.Treeview(frame, show="headings")
            tree.pack(expand=True, fill="both", padx=15, pady=15)

            # Button row
            btnf = tk.Frame(frame, bg="#0A2647")
            btnf.pack(pady=15)
            tk.Button(btnf, text="Refresh", bg="#205295", fg="white",
                      command=lambda table=t: self.load_table(table)).pack(side="left", padx=15)
            tk.Button(btnf, text="Update", bg="#205295", fg="white",
                      command=lambda table=t: self.update_record(table)).pack(side="left", padx=15)
            tk.Button(btnf, text="Delete", bg="#B80000", fg="white",
                      command=lambda table=t: self.delete_record(table)).pack(side="left", padx=15)

            self.trees[t] = tree
            self.load_table(t)

    # ---------------- Helper Methods ----------------
    def get_table_list(self):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")
        rows = [r[0] for r in cur.fetchall()]
        conn.close()
        preferred = ["users", "bookings", "room_service", "payments"]
        ordered = [t for t in preferred if t in rows] + [t for t in rows if t not in preferred]
        return ordered

    def get_columns_for_table(self, table):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(f"PRAGMA table_info({table})")
        cols = [row[1] for row in cur.fetchall()]
        conn.close()
        return cols

    def load_table(self, table):
        tree = self.trees[table]
        for c in tree.get_children():
            tree.delete(c)
        cols = self.get_columns_for_table(table)
        tree["columns"] = cols
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor="center")
        conn = connect_db()
        cur = conn.cursor()
        try:
            cur.execute(f"SELECT * FROM {table}")
            rows = cur.fetchall()
        except Exception as e:
            messagebox.showerror("DB Error", f"Could not load {table}: {e}")
            conn.close()
            return
        conn.close()
        for r in rows:
            tree.insert("", "end", values=r)

    def delete_record(self, table):
        tree = self.trees[table]
        sel = tree.focus()
        if not sel:
            messagebox.showwarning("Select", "Please select a record to delete.")
            return
        vals = tree.item(sel, "values")
        cols = self.get_columns_for_table(table)
        if "id" in cols:
            idx = cols.index("id")
            rec_id = vals[idx]
            confirm = messagebox.askyesno("Confirm", f"Delete record id={rec_id} from {table}?")
            if not confirm:
                return
            conn = connect_db()
            cur = conn.cursor()
            try:
                cur.execute(f"DELETE FROM {table} WHERE id=?", (rec_id,))
                conn.commit()
                conn.close()
                self.load_table(table)
                messagebox.showinfo("Deleted", "Record deleted.")
            except Exception as e:
                conn.close()
                messagebox.showerror("DB Error", f"Could not delete: {e}")
        else:
            messagebox.showerror("No ID", "Table has no 'id' column — cannot delete by id.")

    def update_record(self, table):
        tree = self.trees[table]
        sel = tree.focus()
        if not sel:
            messagebox.showwarning("Select", "Please select a record to update.")
            return
        vals = list(tree.item(sel, "values"))
        cols = self.get_columns_for_table(table)
        if "id" not in cols:
            messagebox.showerror("No ID", "Table has no 'id' column — cannot update by id.")
            return
        rec_id = vals[cols.index("id")]

        up = tk.Toplevel(self.root)
        up.title("Update Record")
        up.geometry("450x400")
        up.configure(bg="white")

        entries = {}
        for i, col in enumerate(cols):
            if col == "id":
                continue
            tk.Label(up, text=col, bg="white").pack(pady=4)
            e = tk.Entry(up)
            e.pack(pady=4, padx=6, fill="x")
            try:
                idx = cols.index(col)
                e.insert(0, vals[idx])
            except Exception:
                pass
            entries[col] = e

        def save_changes():
            set_clause = ", ".join([f"{c}=?" for c in entries.keys()])
            values = [e.get() for e in entries.values()]
            values.append(rec_id)
            conn = connect_db()
            cur = conn.cursor()
            try:
                cur.execute(f"UPDATE {table} SET {set_clause} WHERE id=?", tuple(values))
                conn.commit()
                conn.close()
                up.destroy()
                self.load_table(table)
                messagebox.showinfo("Updated", "Record updated successfully.")
            except Exception as e:
                conn.close()
                messagebox.showerror("DB Error", f"Could not update: {e}")

        tk.Button(up, text="Save Changes", bg="#205295", fg="white",
                  command=save_changes).pack(pady=16)


# ---------------- Passkey Window ----------------
def open_admin_dashboard():
    root = tk.Tk()
    app = AdminDashboard(root)
    root.mainloop()


def ask_admin_passkey():
    win = tk.Tk()
    win.title("Admin Login")
    win.geometry("400x200")
    win.config(bg="#0A2647")

    tk.Label(win, text="🔑  Admin Passkey Required", bg="#0A2647", fg="white",
             font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(win, text="Enter Passkey:", bg="#0A2647", fg="white",
             font=("Arial", 11)).pack(pady=6)
    entry = tk.Entry(win, show="*", font=("Arial", 12), width=25)
    entry.pack(pady=5)

    def check_key():
        if entry.get() == "admin123":  # your passkey
            win.destroy()
            open_admin_dashboard()
        else:
            messagebox.showerror("Access Denied", "Invalid passkey! Try again.")

    tk.Button(win, text="Login", bg="#205295", fg="white", width=12, font=("Arial", 11, "bold"),
              command=check_key).pack(pady=12)

    win.mainloop()


if __name__ == "__main__":
    ask_admin_passkey()

