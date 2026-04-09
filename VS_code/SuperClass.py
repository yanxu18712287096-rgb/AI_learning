from re import fullmatch


class employee:
    def __init__(self,name,eid):
        self.name=name
        self.eid=eid

    def print_message(self):
        print(self.name,self.eid)

class FullTime(employee):
    def __init__(self,name,eid,moth_money):
        super().__init__(name, eid)
        self.moth_money = moth_money

    def calculate_moth_money(self):
        return self.moth_money

class partTime(employee):
    def __init__(self,name,eid,day_money,workday):
        super().__init__(name, eid)
        self.day_money = day_money
        self.workday = workday

    def caluculate_monthly_pay(self):
        return self.day_money * self.workday

zhangsan = FullTime("张三", 1001, 10000)
lisi = partTime("李四", 1002, 100, 30)
zhangsan.print_message()
lisi.print_message()
print(zhangsan.calculate_moth_money())
print(lisi.caluculate_monthly_pay())
