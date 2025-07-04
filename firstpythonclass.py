

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


    # Define food items and their calories
calorie_chart = {
    "egg": 70,
    "carrot": 20,
    "nutella": 1.0,         # per gram
    "toast": 80,
    "banana": 90,
    "chicken breast": 1.65, # per gram
    "rice": 200,
    "apple": 95,
    "milk": 120,
    "yogurt": 1.0           # per gram
}

# Which food uses grams vs units
unit_type = {
    "egg": "unit",
    "carrot": "unit",
    "nutella": "g",
    "toast": "unit",
    "banana": "unit",
    "chicken breast": "g",
    "rice": "unit",
    "apple": "unit",
    "milk": "unit",
    "yogurt": "g"
}

def get_calories(meal):
    food = input(f"\nEnter a food item for {meal}: ").strip().lower()
    quantity = float(input("Enter quantity (e.g., 2 eggs, 100g Nutella): "))
    
    # normalize food
    if food.endswith('s') and food not in calorie_chart:
        food = food[:-1]

    if food in calorie_chart:
        unit = unit_type[food]
        if unit == "g":
            calories = quantity * calorie_chart[food]
        else:
            calories = quantity * calorie_chart[food]
    else:
        print(f"Unknown food item: {food}")
        return 0
    print(f"{meal.capitalize()} Calories: {calories:.2f} kcal")
    return calories

print("Welcome to the Meal Calorie Calculator!")
print("Available food items:")
print("Egg, Carrot, Nutella (100g), Toast, Banana, Chicken Breast (100g), Rice, Apple, Milk, Yogurt (100g)")

# Get calories for each meal
breakfast = get_calories("breakfast")
lunch = get_calories("lunch")
dinner = get_calories("dinner")

total = breakfast + lunch + dinner

print(f"\nTotal Calories for the Day: {total:.2f} kcal")



celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")

word = input("Enter a word: ").strip().lower()

if word and word[0] in "aeiou":
    print(f"'{word}' starts with a vowel.")
else:
    print(f"'{word}' does not start with a vowel.")
    