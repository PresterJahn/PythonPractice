from employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, name, department, hourly_rate, hours_worked):
        super().__init__(name, department, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.hourly_rate * self.hours_worked
