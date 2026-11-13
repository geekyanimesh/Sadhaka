class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

class Cow:

    def sound(self):
        print("Moo")

sounds = [Dog(), Cat(), Cow()]

for i in sounds:
    i.sound()


# Method overloading

class Operations:

    def add(self,a,b,c=0):  # or def add(self, 8args)
        return a+b+c        #       return sum(args)


sum=Operations()

print(sum.add(3,4))
print(sum.add(3,4,5))

