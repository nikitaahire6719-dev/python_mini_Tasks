from company import Company
company = Company("TechCorp")

while True:
    print("\n======Employee payroll system======")
    print("1. Add Employee")
    print("2. Pay Employee")
    print("3. Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            emp_id = int(input("Enter employee ID: "))
            name = input("Enter name: ")
            salary = float(input("Enter base salary: "))
            company.add_employee(emp_id, name, salary)

        case "2":
            emp_id = int(input("Enter employee ID: "))
            bonus = float(input("Enter bonus: "))
            deduction = float(input("Enter deduction: "))
            company.pay_employee(emp_id, bonus, deduction)

        case "3":
            print("System closed")
            break
        
        case _:
            print("Invalid choice")