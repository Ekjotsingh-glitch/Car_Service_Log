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

  
    db.close()


if __name__ == "__main__":
    main()
