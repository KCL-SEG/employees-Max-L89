"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class MonthlyEmployee:
    def __init__(self, name, salary, bonus, contract, per_contract):
        self.salary = salary
        self.name = name
        self.contract = contract
        self.bonus = bonus
        self.per_contract = per_contract

    def get_pay(self):
        return self.salary + self.bonus + self.per_contract* self.contract


    def __str__(self):
        text = f"{self.name} works on a monthly salary of {self.salary}"
        if self.bonus != 0:
            text += f" and receives a bonus commission of {self.bonus}"
        elif self.per_contract != 0:
            text += f" and receives a commission for {self.contract} contract(s) at {self.per_contract}/contract"
        text += f". Their total pay is {self.get_pay()}."
        return text



class HourlyEmployee:
    def __init__(self, name, hour_salary, hours_work,bonus, contract, per_contract):
        self.hour_salary = hour_salary
        self.name = name
        self.hours_work = hours_work
        self.contract = contract
        self.bonus = bonus
        self.per_contract = per_contract


    def get_pay(self):
        return self.hour_salary * self.hours_work + self.bonus + self.per_contract* self.contract

    def __str__(self):
        text1 = f"{self.name} works on a contract of {self.hours_work } hours at {self.hour_salary }/hour"
        if self.bonus != 0:
            text1 += f" and receives a bonus commission of {self.bonus}"
        elif self.per_contract != 0:
            text1 += f" and receives a commission for {self.contract} contract(s) at {self.per_contract}/contract"
        text1 += f". Their total pay is {self.get_pay()}."
        return text1







# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee('Billie',4000,0,0,0)
print(billie.get_pay())
print(billie.__str__())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie',25,100,0,0,0)
print(charlie.get_pay())
print(charlie.__str__())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee('Renee',3000,0,4,200)
print(renee.get_pay())
print(renee.__str__())

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan',25,150,0,3,220)
print(jan.get_pay())
print(jan.__str__())

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee('Robbie',2000,1500,0,0)


# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel',30,120,600,0,0)
