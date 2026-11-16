from employee import Employee
from hourly_employee import HourlyEmployee
from salary_employee import SalaryEmployee
from commission_employee import CommissionEmployee


def load_employees():
    # Pay figures are example annual totals based on the assignment output.
    employees = [
        HourlyEmployee("Nick DeFalco", "Sales", 25, 2080),
        SalaryEmployee("Applejack Johnson", "Sales", 44000),
        SalaryEmployee("Mario Dubois", "Sales", 77200),
        SalaryEmployee("Anthony Jo", "Engineering", 98000),
        Employee("Stephanie Johnson", "Engineering", 31200),
        CommissionEmployee("Dominic Togo", "Maintenance", 20000, 150000, 0.30),
        HourlyEmployee("Christina Gonzalez", "Maintenance", 19.80, 2080),
        HourlyEmployee("Geoffrey Day", "HR", 65, 2080),
    ]
    return employees


def main():
    employees = load_employees()

    # Use the department as each dictionary key.
    employee_dict = {}
    for emp in employees:
        if emp.department not in employee_dict:
            employee_dict[emp.department] = []
        employee_dict[emp.department].append(emp)

    for department, emp_list in employee_dict.items():
        print(f"Department: {department}")
        total_payroll = 0

        for emp in emp_list:
            pay = emp.get_pay()  # Calls the appropriate subclass method.
            total_payroll += pay
            label = emp.__class__.__name__.replace("Employee", " Employee").strip()
            print(f"    {emp} ({label}): ${pay:.2f}")

            # Only commission employees have this special method.
            if isinstance(emp, CommissionEmployee):
                base, commission = emp.get_commission_breakdown()
                percent = commission / pay * 100 if pay else 0
                print(f"        Base ${base:.2f} + Commission ${commission:.2f} "
                      f"({percent:.1f}% of earnings)")

        print(f"Total Payroll: ${total_payroll:.2f}\n")


if __name__ == "__main__":
    main()
