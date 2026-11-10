
# num=int(input('Enter a number: '))

# try:
#     result=100/num
#     print(result)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Num was not zero")

# finally:
#     print("Calculation completed")


age = 5

if age<0:
    raise ValueError("Age cannot be negative")

print("Valid age")

def withdraw(balance, amount):

    if amount <= 0:
        raise ValueError("Withdrawal must be positive")

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount


print(withdraw(1000, 200))

