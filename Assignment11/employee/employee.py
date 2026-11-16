class Employee:
    def __init__(self, name, department, annual_pay):
        self.name = name
        self.department = department
        self.annual_pay = annual_pay

    def get_pay(self):
        return self.annual_pay

    def __str__(self):
        return self.name
