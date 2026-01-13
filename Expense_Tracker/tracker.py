from file_manager import save_expense, read_expenses

class ExpenseTracker:
    def add_expense(self, expense):
        save_expense(expense)
        print("Expense added successfully. ")

    def view_expenses(self):
        expenses = read_expenses()
        if not expenses:
            print("No expenses recorded: ")
            return
        
        print("\n---- Expense List----")
        for amount, category, desc in expenses:
            print(f"{amount} | {category} | {desc}")
        
    def total_expense(self):
        expenses = read_expenses()
        total = sum(float(exp[0])for exp in expenses)
        print(f"\nTotal Expense: {total}")