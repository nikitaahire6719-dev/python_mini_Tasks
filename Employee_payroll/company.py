from employee import Employee
from salary import payroll

class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
        self.payroll = payroll()

    def add_employee(self, emp_id, name, base_salary):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("employee already exists")
                return
            
        emp = Employee(emp_id, name, base_salary)
        self.employees.append(emp)
        print("Employee added successfully")

    def pay_employee(self, emp_id, bonus=0, deduction=0):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                final_salary = self.payroll.calculate_salary(emp.base_salary, bonus, deduction)
                print("\n-------salary deposit-------")
                print(f"Company   : {self.company_name}")
                print(f"Employee  : {emp.name}")
                print(f"Base pay  : {emp.base_salary}")
                print(f"Bonus     : {bonus}")
                print(f"Deduction : {deduction}")
                print(f"Deposited : {final_salary}")
                return
            
        print("Employee not found")

