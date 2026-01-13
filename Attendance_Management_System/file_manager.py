import csv
import os

FILE_NAME = "attendance.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["student ID", "Name", "Status"])

def write_attendance(student_id, name, status):
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, status])

def read_attendance():
    with open(FILE_NAME, mode="r") as file:
        return file.read()