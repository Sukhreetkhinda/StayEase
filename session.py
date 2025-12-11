import os

SESSION_FILE = "session.txt"


def set_user_email(email: str) -> None:
    """Save logged-in user's email."""
    try:
        with open(SESSION_FILE, "w", encoding="utf-8") as f:
            f.write(email.strip())
    except Exception as e:
        print("Error saving session email:", e)


def get_user_email() -> str | None:
    """Return saved email or None."""
    try:
        if not os.path.exists(SESSION_FILE):
            return None
        with open(SESSION_FILE, "r", encoding="utf-8") as f:
            email = f.read().strip()
            return email if email else None
    except Exception as e:
        print("Error reading session email:", e)
        return None
