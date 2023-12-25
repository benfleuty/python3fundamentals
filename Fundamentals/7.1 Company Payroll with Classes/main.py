from company import Company
from employee import Employee


def main():
    my_company = Company()

    new_employee = Employee("Ben", "Fleuty", 30000)
    my_company.add_employee(new_employee)

    new_employee = Employee("John", "Doe", 123450)
    my_company.add_employee(new_employee)

    new_employee = Employee("Jane", "Smith", 78901)
    my_company.add_employee(new_employee)

    my_company.display_employees()


main()