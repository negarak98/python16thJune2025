

# 2. Ask user input
name = input("\nWhat is your name? ")
job = input("Thank you, what is your job? ")
salary = input("What is your salary? ")
location = input("Where are you located? ")

# 3. Output final message
print(f"\nI, {name}, from {location}, working as a {job}, with the salary of {salary}, would love to work in cloud and AI.")

# Print prime numbers from 1 to 100

print("Prime numbers from 1 to 100 are:")

for num in range(2, 101):  # Start from 2, as 1 is not a prime number
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


        balance = 0
welcome = input("Welcome to BDC would you like do deposit (d), withdraw (w), check balance (b), exit (e)? ")

if welcome == "d":
    deposit = int(input("How much would you like to deposit? "))
    balance = balance + deposit
    print("Deposited successfully!")

elif welcome == "w":
    withdraw = int(input("How much would you like to withdraw? "))
    balance = balance - withdraw
    print("Your balance is now: " + str(balance))

elif welcome == "b":
    print(balance)

    print("Welcome to the Investment Options System!")
print("Available investment options:")
print("1. Fixed Deposit: Minimum $100")
print("2. Stock Market Fund: Minimum $200")
print("3. Crypto Basket: Minimum $50")

option = int(input("Choose an option (1–3): "))
amount = float(input("Enter investment amount: "))

if option == 1:
    if amount < 100:
        print("Minimum amount for Fixed Deposit is $100.")
    else:
        print("Investment in Fixed Deposit confirmed.")
elif option == 2:
    if amount < 200:
        print("Minimum amount for Stock Market Fund is $200.")
    else:
        print("Investment in Stock Market Fund confirmed.")
elif option == 3:
    if amount < 50:
        print("Minimum amount for Crypto Basket is $50.")
    else:
        print("Investment in Crypto Basket confirmed.")
else:
    print("Invalid option selected.")


    
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")

word = input("Enter a word: ").strip().lower()

if word and word[0] in "aeiou":
    print(f"'{word}' starts with a vowel.")
else:
    print(f"'{word}' does not start with a vowel.")









def add_three_numbers(a, b, c):
    return a + b + c

result_of_three_number = add_three_numbers(10, 5, 10)
print("The sum of three numbers is:", result_of_three_number)





def add_numbers(a, b):
    return int(a + b)

# Taking input from user and adding two numbers
number1 = int(input("Give me the first number: "))
number2 = int(input("Give me the second number: "))
addition = add_numbers(number1, number2)
print("The sum is", addition)
