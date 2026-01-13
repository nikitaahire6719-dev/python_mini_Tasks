import csv
import os

FILE_NAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Description"])

def save_expense(expense):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([expense.amount, expense.category, expense.description])

def read_expenses():
    expenses = []
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            expenses.append(row)
    return expenses
