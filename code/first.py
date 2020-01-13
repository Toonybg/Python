print("-------------------")

class Employee:
    raise_amount = 1.04

    def __init__(self,name,lastname,pay):
        self.name = name
        self.lastname = lastname
        self.email = name + lastname + "@company.com"
        self.pay = pay

emp_1 = Employee("Toony","bg",48000)

print(emp_1.email)






print("-------------------")