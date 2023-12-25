from employee import Employee


class Company:
    def __init__(self):
        self.employees: Employee = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print(f"Current Employees: {len(self.employees)}")
        for e in self.employees:
            print(f"{e.first_name} {e.last_name}")

        print()

    def pay_employees(self):
        print("Paying Employees:")
        currency_symbol = "£"
        for e in self.employees:
            print(f"Paying {e.first_name} {e.last_name} {currency_symbol}{e.calculate_paycheck():,.2f}")
        
        print()