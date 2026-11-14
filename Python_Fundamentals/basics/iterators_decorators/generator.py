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

squares = (x * x for x in range(5))

print(next(squares))  # 0
print(next(squares))  # 1

