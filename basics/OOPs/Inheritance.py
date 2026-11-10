
class Employee:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name, self.age)

class Dev(Employee):

    def write_Code(self):
        print("Devs write code")

d = Dev("Animesh",21)
d.display()
d.write_Code()

# Multiple Inheritance

class Father:

    def skills(self):
        print("Gardening")

class Mother:

    def talent(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()

c.talent()
c.skills()

# Method overrding

class Animal:

    def sound(self):
        print("Animal sound")

class Dog(Animal):

    def __init__(self):
        pass

    def sound(self):
        print("Bark")

d = Dog()
d.sound()

# MRO - Method Resolution Order

class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class D(B, C):
    pass


obj = D()

obj.show()

print(D.mro())


# Inheritance represents an "is-a" relationship.

# For example:
# - Dog is an Animal.
# - Developer is an Employee.
# Composition represents a "has-a" relationship.

# For example:
# - Car has an Engine.
# - Computer has a Processor.

