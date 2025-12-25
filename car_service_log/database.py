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

   