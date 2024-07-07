# QYESTION 1:
def calculate_grade(score):
    if score > 100 or score < 0:
        return 'Invalid score'
    elif score >= 90:
        return 'A+'
    elif score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    elif score >= 40:
        return 'E'
    else:
        return 'F'

def print_marksheet(name, score, grade):
    print("Marksheet")
    print("---------")
    print(f"Student Name: {name}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")
name = input("Enter the student's name: ")
try:
    score = float(input("Enter the student's score: "))
    if score > 100:
        raise ValueError("Score cannot be greater than 100.")
except ValueError as e:
    print(e)
    exit()

grade = calculate_grade(score)
print_marksheet(name, score, grade)

# QUESTION:2
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Question 3
def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

def fahrenheit_to_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)

def celsius_to_kelvin(celsius):
    return celsius + 273.15

print("Choose a conversion:") 
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")
print("3: Celsius to Kelvin")

choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("Temperature in Fahrenheit:", fahrenheit)
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print("Temperature in Celsius:", celsius)
elif choice == 3:
    celsius = float(input("Enter temperature in Celsius: "))
    kelvin = celsius_to_kelvin(celsius)
    print("Temperature in Kelvin:", kelvin)
else:
    print("Invalid choice")

# QUESTION 4
def determine_triangle_type(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "Invalid Triangle: All side lengths must be positive."
    elif side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
        return "Invalid Triangle: The given sides do not form a triangle."
    if side1 == side2 == side3:
        return "Equilateral Triangle"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

try:
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

triangle_type = determine_triangle_type(side1, side2, side3)
print("The triangle is a:", triangle_type)
