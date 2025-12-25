import sqlite3
import os


class Database:
    def __init__(self, db_path):
        folder = os.path.dirname(db_path)
        if folder != "":
            os.makedirs(folder, exist_ok=True)

        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor() 

        self.conn.execute("PRAGMA foreign_keys = ON")
        self.create_tables()

    def create_tables(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate TEXT UNIQUE NOT NULL,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL
        )
        """)

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS service_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            mileage INTEGER NOT NULL,
            service_type TEXT NOT NULL,
            cost REAL NOT NULL,
            notes TEXT,
            FOREIGN KEY (car_id) REFERENCES cars(id) ON DELETE CASCADE
        )
        """)

        self.conn.commit()

    def close(self):
        self.conn.close()
