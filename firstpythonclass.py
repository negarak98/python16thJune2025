



def add_numbers(a, b):
    return int(a + b)

# Taking input from user and adding two numbers
number1 = int(input("Give me the first number: "))
number2 = int(input("Give me the second number: "))
addition = add_numbers(number1, number2)
print("The sum is", addition)


def add_numbers(current_sum, number):#36,23
    return current_sum + number#36,23 reutn 59
 
i = True
total_sum = 0
 
while i == True:
    number = int(input("Input a number: "))
    total_sum = add_numbers(total_sum, number)#add_numbers(24,12)=36,23 add_numbers(36,23)=59, add_numbers(59,48)
    validation = input("Do you want to enter another number? (Yes/No): ")    
    if validation.lower() == "yes":
        continue
    else:
        print("Final Sum:", total_sum)
        print("Bye Bye!!")
        break
 
def check_palindrome():
    text = input("Enter a word or phrase: ")
    cleaned = ''.join(text.lower().split())
 
    if cleaned == cleaned[::-1]:
        print(f'"{text}" is a palindrome.')
    else:
        print(f'"{text}" is not a palindrome.')
 
check_palindrome()

 
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