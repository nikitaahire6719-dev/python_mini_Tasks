from expense import Expense
from tracker import ExpenseTracker
from file_manager import initialize_file

def main():
    initialize_file()
    tracker = ExpenseTracker()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. View Total Expense")
        print("4. Exit")
        
        choice = input("Enter choice: ")

        match choice:
            case "1":
                amount = float(input("Enter amount: "))
                category = input("Enter Category: ")
                description = input("Enter description: ")

                expense = Expense(amount, category, description) 
                tracker.add_expense(expense)

            case "2":
                tracker.view_expenses()

            case "3":
                tracker.total_expense()

            case "4":
                print("Exiting Expense Tracker.")
                break

            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()