



def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def calculator():
    while True:
        op = input("Choose operation (+, -, *, / or type 'exit' to quit): ")
        
        if op.lower() == "exit":
            print("Goodbye!")
            break

        # Ask for numbers
        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        # Choose operation
        if op == "+":
            print("Result:", add(a, b))
        elif op == "-":
            print("Result:", subtract(a, b))
        elif op == "*":
            print("Result:", multiply(a, b))
        elif op == "/":
            print("Result:", divide(a, b))
        else:
            print("Invalid operation.")
