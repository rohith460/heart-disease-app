import hashlib
from database import get_db

def hash_password(p):
    return hashlib.sha256(p.encode()).hexdigest()

def register_user(u, p):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO users (username,password) VALUES (?,?)",
            (u, hash_password(p))
        )
        conn.commit()
        return True
    except:
        return False

def login_user(u, p):
    conn = get_db()
    c = conn.cursor()
    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (u, hash_password(p))
    )
    return c.fetchone()
