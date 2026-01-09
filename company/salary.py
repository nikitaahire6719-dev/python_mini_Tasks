class payroll:
    def calculate_salary(self, base_salary, bonus=0, deduction=0):
        final_amount = base_salary + bonus - deduction
        return final_amount