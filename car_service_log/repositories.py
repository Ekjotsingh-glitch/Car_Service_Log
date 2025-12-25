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

    def get_car_id_by_plate(self, plate):
        self.db.cur.execute(
            "SELECT id FROM cars WHERE plate = ?",
            (plate,)
        )
        row = self.db.cur.fetchone()
        if row is None:
            return None
        return row[0]


class ServiceRepository:
    def __init__(self, db):
        self.db = db

    def add_service(self, car_id, date, mileage, service_type, cost, notes):
        self.db.cur.execute("""
            INSERT INTO service_records (car_id, date, mileage, service_type, cost, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (car_id, date, mileage, service_type, cost, notes))
        self.db.conn.commit()

    def all_services(self):
        self.db.cur.execute("""
        SELECT sr.id, c.plate, sr.date, sr.mileage, sr.service_type, sr.cost
        FROM service_records sr
        JOIN cars c ON c.id = sr.car_id
        ORDER BY sr.date DESC
        """)
        return self.db.cur.fetchall()
    
    def history_for_car(self, car_id):
        self.db.cur.execute("""
            SELECT id, date, mileage, service_type, cost, COALESCE(notes,'')
            FROM service_records
            WHERE car_id = ?
            ORDER BY date DESC, mileage DESC
        """, (car_id,))
        return self.db.cur.fetchall()

    def delete_record(self, rec_id):
        self.db.cur.execute(
            "DELETE FROM service_records WHERE id = ?",
            (rec_id,)
        )
        self.db.conn.commit()
        return self.db.cur.rowcount

