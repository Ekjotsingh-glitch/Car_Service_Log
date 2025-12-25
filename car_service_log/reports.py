import csv
import os
from openpyxl import Workbook

HEADERS = ["id", "plate", "date", "mileage", "service_type", "cost"]


def export_to_csv(rows, path):
    folder = os.path.dirname(path)
    if folder != "":
        os.makedirs(folder, exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)
        for row in rows:
            writer.writerow(row)



