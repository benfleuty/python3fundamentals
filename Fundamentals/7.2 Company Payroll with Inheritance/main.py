from company import Company
from employees.hourly_employee import HourlyEmployee
from employees.salary_employee import SalaryEmployee
from employees.commision_employee import CommisionEmployee


def main():
    my_company = Company()

    new_employee = SalaryEmployee("Ben", "Fleuty", 30000)
    my_company.add_employee(new_employee)

    new_employee = SalaryEmployee("John", "Doe", 123450)
    my_company.add_employee(new_employee)

    new_employee = SalaryEmployee("Jane", "Smith", 78901)
    my_company.add_employee(new_employee)

    new_employee = HourlyEmployee("Some", "Guy", 45, 10.01)
    my_company.add_employee(new_employee)

    new_employee = CommisionEmployee("A", "Worker", 22000, 8, 55)
    my_company.add_employee(new_employee)

    my_company.display_employees()

    my_company.pay_employees()


main()
