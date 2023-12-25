from employees.salary_employee import SalaryEmployee


class CommisionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, total_sales, com_rate):
        super().__init__(fname, lname, salary)
        self.total_sales = total_sales
        self.com_rate = com_rate
        self.salary = salary

    def calculate_paycheck(self) -> float:
        monthly_salary = self.salary / 12
        commision = self.total_sales * self.com_rate
        return monthly_salary + commision
