def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(a, b):
    return a ** b

def digits():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a, b

def calPrompt():
    while True:
        operation = input("What operation would you like to perform? ").lower()

        if operation == "add":
            a, b = digits()
            print(add(a,b))
        elif operation == "subtract":
            a, b = digits()
            print(subtract())
        elif operation == "multiply":
            a, b = digits()
            print(multiply())
        elif operation == "divide":
            a, b = digits()
            print(divide())
        elif operation == "power":
            a, b = digits()
            print(power())
        elif operation == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid input, please try again.")

calPrompt()
