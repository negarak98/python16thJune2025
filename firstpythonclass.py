
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