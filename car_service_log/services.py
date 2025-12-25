import sqlite3


class CarServiceApp:
    def __init__(self, car_repo, service_repo):
        self.car_repo = car_repo
        self.service_repo = service_repo

    def add_car(self):
        plate = input("Plate: ").strip()
        brand = input("Brand: ").strip()
        model = input("Model: ").strip()
        year_text = input("Year: ").strip()

        if not year_text.isdigit():
            print("Year must be a number.")
            return

        if self.car_repo.plate_exists(plate):
            print("That plate already exists.")
            return

        self.car_repo.add_car(plate, brand, model, int(year_text))
        print("Car added!")

    def list_cars(self):
        cars = self.car_repo.list_cars()
        if len(cars) == 0:
            print("No cars found.")
            return

        print("Cars:")
        for car_id, plate, brand, model, year in cars:
            print(f"- {plate}: {brand} {model} ({year})")

    def add_service(self):
        plate = input("Plate of the car: ").strip()
        car_id = self.car_repo.get_car_id_by_plate(plate)

        if car_id is None:
            print("Car not found. Add the car first.")
            return

        date = input("Date (YYYY-MM-DD): ").strip()
        mileage_text = input("Mileage: ").strip()
        service_type = input("Service type (oil change, brakes...): ").strip()
        cost_text = input("Cost: ").strip()
        notes = input("Notes (optional): ").strip()

        if not mileage_text.isdigit():
            print("Mileage must be a number.")
            return

        try:
            mileage = int(mileage_text)
            cost = float(cost_text)
        except ValueError:
            print("Cost must be a number (example: 79.99).")
            return

        self.service_repo.add_service(car_id, date, mileage, service_type, cost, notes)
        print("Service record added!")

    def show_history(self):
        plate = input("Plate: ").strip()
        car_id = self.car_repo.get_car_id_by_plate(plate)

        if car_id is None:
            print("Car not found.")
            return

        records = self.service_repo.history_for_car(car_id)
        if len(records) == 0:
            print("No service records for this car.")
            return

        print(f"Service history for {plate}:")
        for rec_id, date, mileage, service_type, cost, notes in records:
            print(f"[{rec_id}] {date} - {mileage} km - {service_type} - €{cost:.2f}")
            if notes != "":
                print("   Notes:", notes)

    def delete_service(self):
        rec_id_text = input("Record id to delete: ").strip()
        if not rec_id_text.isdigit():
            print("Id must be a number.")
            return

        deleted = self.service_repo.delete_record(int(rec_id_text))
        if deleted == 0:
            print("No record deleted (id not found).")
        else:
            print("Record deleted.")
