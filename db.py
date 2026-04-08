import sqlite3

def connect_db():
    try:
        conn = sqlite3.connect("football.db")
        return conn
    except Exception as e:
        print("❌ Database connection error:", e)