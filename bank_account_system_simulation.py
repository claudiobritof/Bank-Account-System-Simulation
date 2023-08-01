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