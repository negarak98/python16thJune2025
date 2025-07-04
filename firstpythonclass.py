
print("hello world")
print ( [1,2,3,4,5,6,7,8,9,10])

name = input ("what is your name?")
print("hello, " + name + "!")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)

for i in range(1, 11):

    print(i)

 
a = 5

b = 10

c = 3

print("Largest is", max(a, b, c))


num = int(input("Enter a number: "))

if num % 2 == 0:

    print("free to go")

else:

    print("you are in prison")
 


# 1. Print numbers from 1 to 1000
for i in range(1, 1001):
    print(i)

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