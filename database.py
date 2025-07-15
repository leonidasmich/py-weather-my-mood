import sqlite3
import pandas as pd

DB_NAME = "mood_logs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS mood_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            text TEXT NOT NULL,
            mood TEXT NOT NULL,
            weather TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_log(timestamp, text, mood, weather):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO mood_logs (timestamp, text, mood, weather)
        VALUES (?, ?, ?, ?)
    ''', (timestamp.isoformat(), text, mood, weather))
    conn.commit()
    conn.close()

def get_all_logs():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM mood_logs ORDER BY timestamp DESC", conn)
    conn.close()
    return df
