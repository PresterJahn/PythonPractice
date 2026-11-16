from employee import Employee


class CommissionEmployee(Employee):
    def __init__(self, name, department, base_pay, sales, commission_rate):
        super().__init__(name, department, base_pay)
        self.sales = sales
        self.commission_rate = commission_rate

    def get_commission_breakdown(self):
        commission = self.sales * self.commission_rate
        return self.annual_pay, commission

    def get_pay(self):
        base, commission = self.get_commission_breakdown()
        return base + commission
