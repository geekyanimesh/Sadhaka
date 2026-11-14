
class Car:

    def start(self):
        print("Car has started")

    def accelerate(self):
        print("Car is accelerating.")

c1=Car()

c1.accelerate()
c1.start()


# Constructor

class Student:

    def __init__(self,name,age,roll_number):
        self.name=name
        self.age=age
        self.roll_number=roll_number


student1 = Student("Animesh",21,6)

print(student1.name)
print(student1.age)

# Python internally passes the newly created object as the first argument to __init__().
# like Student.__init__(student1, "Rahul", 21, 101)

class Bank:

    def __init__(self,balance,name):
        self.name=name
        self.__balance=balance

b = Bank(10000,"Animesh")

print(b.__balance)
        