import calc, math, random as rnd

def sum (a,b):
    return a+b

print(sum(5,6))

# f-string
def introduce(name, age):
    print(f"{name} is {age}.")

introduce("Animesh",21)

def greeting(name, greeting="Hello"):
    return f"{greeting}, {name}"

print(greeting("hey","Animesh"))

# return v/s print

def first():
    print(10)

def second():
    return 10

x = first()
y = second()

print("x =", x)
print("y =", y)

def operation(a,b):
    return a+b, a-b

x2=operation(10,7)
print(x2)

sumVal, diffVal=x2
print(sumVal)
print(diffVal)

print(calc.multiply(10,20))

print(math.sqrt(49))

print(rnd.randint(1,10))

x = 10
def f():
    x = 20
f()
print(x)