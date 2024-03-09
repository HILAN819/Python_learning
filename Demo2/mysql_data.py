import json
from pathlib import Path
import mysql.connector
from mysql.connector import Error

students = [
    {"student_id": 12, "first_name": "Hilan", "last_name": "whitaker",
        "email": "hilanwhitaker@email.com", "dateRegistered": "17-02-2024"},
    {"student_id": 13, "first_name": "Josh", "last_name": "Steven",
        "email": "joshsteven@email.com", "dateRegistered": "12-07-2024"}
]

data = json.dumps(students)
# print(data)
Path("students.json").write_text(data, encoding="utf-8")
student_data = json.loads(Path("students.json").read_text(encoding="utf-8"))

# connecting to database and inputing the data

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "SchoolDatabase",
    "port": "3306"

}
conn = None
try:
    conn = mysql.connector.connect(**db_config)

    if conn.is_connected():
        print("Connected to database")

        command = "INSERT INTO students VALUES(?, ?, ?)"

        for student in students:
            conn.execute(command, tuple(student.values()))

        conn.commit()

except Error as e:
    print(f"Error: {e}")

finally:
    if conn is not None and conn.is_connected():
        conn.close()
        print("Connection closed")


# with mysql.connector.connect("SchoolDatabase") as conn:
