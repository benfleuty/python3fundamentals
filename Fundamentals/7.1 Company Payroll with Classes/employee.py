class Employee:
    def __init__(self, fname, lname, salary):
        self.first_name = fname
        self.last_name = lname
        self.salary = salary

    def calculate_paycheck(self) -> float:
        return self.salary / 12
