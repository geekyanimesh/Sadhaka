
def announce(func):
    def wrapper():
        print("Function loading...")
        func()
    return wrapper

@announce
def greet():
    print("Greetings!")

def hello():
    print("Hello!")



greet()