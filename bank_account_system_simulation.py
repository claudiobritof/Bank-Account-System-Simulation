# Simulation of a bank system back-end:

class Account():
    def __init__(self, number, holder_name, balance, limit):
        self.number = number
        self.holder_name = holder_name
        self.balance = balance
        self.limit = limit

    # Creating methods:
    def deposit(self, importance):
        self.balance += importance

    def withdraw(self, importance):
        new_balance = self.balance - importance
        if new_balance < 0:
            print(f'Balance of US$ {self.balance} is insufficient to withdraw US$ {importance}.')
        else:
            self.balance = new_balance

    def increase_limit(self, importance):
        self.limit += importance
        
    def decrease_limit(self, importance):
        self.limit -= importance
    
    def extract(self):
        print(f'Account Number: {self.number}\nHolder Name: {self.holder_name}\nCurrent Balance: US$ {self.balance}\nCurrent Limit: US$ {self.limit}\n')
    
# Creating a class "SavingsAccount" to make balance yield. All related to "account":        
class SavingsAccount(Account):
    def __init__(self, number, holder_name, balance, limit, yield_rate=0.05):
        super().__init__(number, holder_name, balance, limit)
        self.yield_rate = yield_rate
        
    def yielding(self):
        self.balance += self.balance * self.yield_rate

# Creating a "SalaryAccount" class:
class SalaryAccount(Account):
    def __init__(self, number, holder_name, balance, limit, salary):
        super().__init__(number, holder_name, balance, limit)
        self.salary = salary

    def earn(self):
        self.deposit(self.salary)
    
    def new_salary(self, new_salary):
        self.salary = new_salary
    
# Creating a "CheckingAccount" class:
class CheckingAccount(Account):
    def __init__(self, number, holder_name, balance, limit):
        super().__init__(number, holder_name, balance, limit)
        if limit < 0:
            limit = 0
        self.limit = limit 