class CarRepository:
    def __init__(self, db):
        self.db = db

    def add_car(self, plate, brand, model, year):
        self.db.cur.execute(
            "INSERT INTO cars (plate, brand, model, year) VALUES (?, ?, ?, ?)",
            (plate, brand, model, year)
        )
        self.db.conn.commit()
    
   