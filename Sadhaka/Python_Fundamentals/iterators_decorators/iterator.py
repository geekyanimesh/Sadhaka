
numbers = [10,20,30,40]

it=iter(numbers)

print(next(it))
print(next(it))
print(next(it))

# Generators

def count_up_to_three():
    yield 1
    yield 2
    yield 3

for number in count_up_to_three():
    print(number)

# return - ends functions
# yield - pauses functions

def demo():
    print("Start")
    yield 10
    print("Resume")
    yield 20

g = demo()

print(next(g))
print(next(g))

