
def announce(func):
    def wrapper():
        print("hello!")
        func()
        print("end!")
    return wrapper


@announce
def greet():
    print("Greetings!")

greet()   


from functools import wraps

def log_generator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Generating numbers...")

        for num in func(*args, **kwargs):
            print("Generated:", num)
            yield num

    return wrapper


@log_generator
def even_numbers(n):
    for x in range(n):
        if x % 2 == 0:
            yield x


for num in even_numbers(10):
    print(num)