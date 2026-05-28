import sqlite3
from pathlib import Path 

DB_PATH = Path("secure_chat.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row 
    return conn 

def init_db():
    conn = get_connection()
    cursor = conn.cursor() 

    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL, public_key TEXT NOT NULL 
    ) 
    """)
    
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS messages ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    sender TEXT NOT NULL, receiver TEXT NOT NULL, ciphertext TEXT NOT NULL, 
    nonce TEXT NOT NULL, 
    signature TEXT NOT NULL, timestamp INTEGER NOT NULL 
    ) 
    """)

    conn.commit()
    conn.close()