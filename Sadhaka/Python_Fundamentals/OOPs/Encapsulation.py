
class BankAccount:

    def __init__(self, balance):
        self.__balance=balance

    def getBalance(self):
        return self.__balance

    def setBalance(self,amount):

        if amount>0:
            self.__balance=amount
        else:
            print("Invalid Balance")

b= BankAccount(10000)

b.setBalance(20000)
num=b.getBalance()
print(num)


# When is encapsulation useful?
# - Banking systems.
# - User authentication.
# - E-commerce payment systems.
# - Employee management applications.
# - Any application where object state must be controlled.