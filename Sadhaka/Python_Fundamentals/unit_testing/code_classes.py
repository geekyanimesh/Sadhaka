
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b



class BankAccount:

    def __init__(self,amount):
        self.amount=amount

    def deposit(self,balance):
        self.amount+=balance

    def withdraw(self,balance):
        if self.amount>=balance:
            self.amount-=balance
        else:
            return ValueError


