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

   