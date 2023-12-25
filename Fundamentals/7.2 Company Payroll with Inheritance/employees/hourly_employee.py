from employees.employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, hours_worked, hourly_rate):
        super().__init__(fname, lname)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self) -> float:
        return self.hours_worked * self.hourly_rate
