# Car Service Log



## Purpose

A small CLI application to manage cars and their service records.



## Technology

- Python (3.x)

- SQLite (via Python `sqlite3`)



## Libraries

(see `requirements.txt`)

- `openpyxl`: export reports to Excel (`.xlsx`)



## Functions

- Add a car

- List cars

- Add a service record for a car

- Show service history for a car

- Delete a service record

- Export all service records to CSV

- Export all service records to Excel



## Planned functions

- Edit a car

- Edit a service record

- Search / filter service records


## How to execute
Staying in the correct directory is important for the execution : 
```bash
cd (foldername)
```
1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate Virtual Environment :
```bash
.\.venv\Scripts\activate
```
3. Install:
```bash
pip install -r requirements.txt
```
### Database name / settings file
Create a file `settings.py` in the main folder.

Copy `example_settings.py` and rename it to `settings.py`.



Content example:

```python

DB_PATH = "data/car_service.db"

REPORTS_FOLDER = "reports" 

```



## External libraries

(see `requirements.txt`)

- `openpyxl` is used to export `.xlsx` (Excel).

- `sqlite3`, `csv`, and `os` are part of Python (no install needed).



## Project root note (Spyder)



If you get this error (when trying to run the application on spyder):



```text

ModuleNotFoundError: No module named 'settings'

```

Run the program from the project root folder (the folder that contains:

`car_service_log/`, `data/`, `example_settings.py`).



Running the program from Terminal should be no problem:

```bash

python -m car_service_log.main

```





## Structure of the database

The database consists of two tables. 



### Table 1: cars 

```sql

CREATE TABLE cars (

&nbsp;           id INTEGER PRIMARY KEY AUTOINCREMENT,

&nbsp;           plate TEXT UNIQUE NOT NULL,

&nbsp;           brand TEXT NOT NULL,

&nbsp;           model TEXT NOT NULL,

&nbsp;           year INTEGER NOT NULL

&nbsp;      )



```



### Table 2: Service_records

```sql

CREATE TABLE service_records (

&nbsp;           id INTEGER PRIMARY KEY AUTOINCREMENT,

&nbsp;           car_id INTEGER NOT NULL,

&nbsp;           date TEXT NOT NULL,

&nbsp;           mileage INTEGER NOT NULL,

&nbsp;           service_type TEXT NOT NULL,

&nbsp;           cost REAL NOT NULL,

&nbsp;           notes TEXT,

&nbsp;           FOREIGN KEY (car_id) REFERENCES cars(id) ON DELETE CASCADE

&nbsp;       )

```

