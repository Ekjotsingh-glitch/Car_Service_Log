class CarRepository:
    def __init__(self, db):
        self.db = db

    def add_car(self, plate, brand, model, year):
        self.db.cur.execute(
            "INSERT INTO cars (plate, brand, model, year) VALUES (?, ?, ?, ?)",
            (plate, brand, model, year)
        )
        self.db.conn.commit()
    
    def plate_exists(self, plate):
      self.db.cur.execute("SELECT id FROM cars WHERE plate = ?", (plate,))
      row = self.db.cur.fetchone()
      return row is not None

    def list_cars(self):
        self.db.cur.execute(
            "SELECT id, plate, brand, model, year FROM cars ORDER BY brand, model"
        )
        return self.db.cur.fetchall()

 