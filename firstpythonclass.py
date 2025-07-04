


weather = input("How does the weather look today?? ")

if weather == "hot":
    print(" stay hydrated! ")
elif weather == "cold":
    print("grab ur hot drink.")
elif weather == "rainy":
    print("dont forget ur umbrella. 🌧️☔")
else:
    print("Hmm, sorry didn’t get you please try again! ")




# Function to check letter grade
def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Ask how many students
num_students = int(input("Enter the number of students: "))

# Loop through each student
for i in range(num_students):
    print(f"\nStudent {i + 1}")
    name = input("Enter student name: ")
    score = float(input("Enter score (0–100): "))
    
    # Get the grade
    grade = check_grade(score)
    
    # Show result
    print(f"{name} got grade: {grade}")