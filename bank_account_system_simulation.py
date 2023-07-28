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