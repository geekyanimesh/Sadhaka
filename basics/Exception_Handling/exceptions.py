
try:
    a=10
    b=0

    result = a/b
    print(result)

except ZeroDivisionError:
    print("Cannot divide by Zero!")

print("Calculation Completed")

try:
    num = int(input("Enter a number: "))
    result = 100 / num

    print(result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")


try:
    print("Opening file...")
    result = 10 / 0

except ZeroDivisionError:
    print("Error occurred!")

finally:
    print("Cleanup operation completed.")

    