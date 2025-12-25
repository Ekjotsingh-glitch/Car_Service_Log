import os
import settings

from car_service_log.database import Database
from car_service_log.repositories import CarRepository, ServiceRepository
from car_service_log.services import CarServiceApp
from car_service_log.reports import export_to_csv, export_to_excel


def main():
    db = Database(settings.DB_PATH)

    car_repo = CarRepository(db)
    service_repo = ServiceRepository(db)
    app = CarServiceApp(car_repo, service_repo)

    while True:
        print("\n=== Car Service Log ===")
        print("1) Add car")
        print("2) List cars")
        print("3) Add service record")
        print("4) Show service history for a car")
        print("5) Export ALL services to CSV")
        print("6) Export ALL services to Excel")
        print("7) Delete a service record")
        print("0) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            app.add_car()
        elif choice == "2":
            app.list_cars()
        elif choice == "3":
            app.add_service()
        elif choice == "4":
            app.show_history()
        elif choice == "5":
            rows = service_repo.all_services()
            if len(rows) == 0:
                print("No service records to export.")
            else:
                path = os.path.join(settings.REPORTS_FOLDER, "all_services.csv")
                export_to_csv(rows, path)
                print("Saved:", path)

        elif choice == "6":
            rows = service_repo.all_services()
            if len(rows) == 0:
              print("No service records to export.")
            else:
                path = os.path.join(settings.REPORTS_FOLDER, "all_services.xlsx")
                export_to_excel(rows, path)
                print("Saved:", path)


        

        elif choice == "7":
            app.delete_service()
        elif choice == "0":
            break
        else:
            print("Unknown choice.")

    db.close()


if __name__ == "__main__":
    main()
