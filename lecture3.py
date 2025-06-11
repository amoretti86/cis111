# CIS 111 Lecture 3 Overview
# Python Lesson: Input, Processing, Output, Decision Structures & Boolean Logic

# ========== INPUT ==========
# Getting user input - input() always returns a string
name = input("Enter your name: ")
age_str = input("Enter your age: ")

# Converting string input to numbers
age = int(age_str)  # Convert to integer
height = float(input("Enter your height in meters: "))  # Direct conversion

print(f"Hello {name}, you are {age} years old and {height}m tall")

# ========== PROCESSING ==========
# Basic arithmetic operations
salary = 50000
bonus_rate = 0.15
bonus = salary * bonus_rate
total_income = salary + bonus

# String processing
full_name = name.upper()
initials = name[0].upper() if name else ""

# Mathematical processing
import math
bmi = round(70 / (height ** 2), 2)  # Assuming 70kg weight
circle_area = math.pi * (5 ** 2)  # Circle with radius 5

# ========== OUTPUT ==========
# Different ways to output data
print("Basic print:", total_income)
print(f"F-string formatting: Your BMI is {bmi}")
print("Old style formatting: Age in 10 years will be {}".format(age + 10))
print("Multiple values:", name, age, height, sep=" | ")

# Formatted output
print(f"Financial Summary for {name}:")
print(f"  Base Salary: ${salary:,}")
print(f"  Bonus: ${bonus:,.2f}")
print(f"  Total: ${total_income:,.2f}")

# ========== BOOLEAN LOGIC ==========
# Boolean values and variables
is_adult = age >= 18
is_tall = height > 1.8
has_bonus = bonus > 0
is_weekend = True
is_working = False

print(f"\nBoolean values:")
print(f"Is adult: {is_adult}")
print(f"Is tall: {is_tall}")
print(f"Has bonus: {has_bonus}")

# Boolean operators
# AND - both conditions must be True
can_drive = is_adult and has_bonus
print(f"Can afford to drive: {can_drive}")

# OR - at least one condition must be True
can_relax = is_weekend or not is_working
print(f"Can relax: {can_relax}")

# NOT - reverses the boolean value
is_not_adult = not is_adult
print(f"Is not adult: {is_not_adult}")

# Complex boolean expressions
eligible_for_loan = is_adult and (total_income > 40000) and not (age > 65)
print(f"Eligible for loan: {eligible_for_loan}")

# ========== DECISION STRUCTURES ==========

# Simple if statement
if is_adult:
    print("You can vote!")

# if-else statement
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# if-elif-else chain
if age < 13:
    category = "child"
elif age < 20:
    category = "teenager"
elif age < 65:
    category = "adult"
else:
    category = "senior"

print(f"Age category: {category}")

# Nested if statements
if is_adult:
    if total_income > 50000:
        print("You qualify for premium services")
    else:
        print("You qualify for standard services")
else:
    print("Parental consent required")

# Multiple conditions in if statements
if age >= 18 and total_income > 30000 and height > 1.6:
    print("Eligible for special program")

# Using boolean variables in conditions
if has_bonus:
    print("Congratulations on your bonus!")

# Comparison operators
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# ========== PRACTICAL EXAMPLES ==========

# Example 1: Simple calculator with decisions
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

print(f"Result: {result}")

# Example 2: Grade calculator with multiple conditions
test1 = float(input("Enter test 1 score: "))
test2 = float(input("Enter test 2 score: "))
test3 = float(input("Enter test 3 score: "))

average = (test1 + test2 + test3) / 3

print(f"Your average is: {average:.2f}")

if average >= 90 and all([test1 >= 80, test2 >= 80, test3 >= 80]):
    print("Excellent performance!")
elif average >= 80:
    print("Good job!")
elif average >= 70:
    print("Satisfactory")
elif average >= 60:
    print("Needs improvement")
else:
    print("Must retake")

# Example 3: Loan eligibility checker
print("\n--- Loan Eligibility Checker ---")
applicant_age = int(input("Enter your age: "))
annual_income = float(input("Enter annual income: "))
has_job = input("Do you have a job? (yes/no): ").lower() == "yes"
credit_score = int(input("Enter credit score: "))

# Complex boolean logic for loan approval
age_eligible = 18 <= applicant_age <= 70
income_eligible = annual_income >= 25000
employment_eligible = has_job
credit_eligible = credit_score >= 650

# Overall eligibility
loan_approved = age_eligible and income_eligible and employment_eligible and credit_eligible

print(f"\nLoan Application Results:")
print(f"Age eligible: {age_eligible}")
print(f"Income eligible: {income_eligible}")
print(f"Employment eligible: {employment_eligible}")
print(f"Credit eligible: {credit_eligible}")
print(f"LOAN APPROVED: {loan_approved}")

if loan_approved:
    # Determine loan amount based on income
    if annual_income >= 100000:
        max_loan = annual_income * 5
    elif annual_income >= 50000:
        max_loan = annual_income * 4
    else:
        max_loan = annual_income * 3
    
    print(f"Maximum loan amount: ${max_loan:,.2f}")
else:
    print("Loan application denied. Please improve your qualifications.")

# ========== BOOLEAN EXPRESSIONS IN LOOPS ==========
# Using boolean logic to control loops

# While loop with boolean condition
attempts = 0
max_attempts = 3
success = False

while attempts < max_attempts and not success:
    password = input("Enter password: ")
    if password == "secret123":
        success = True
        print("Access granted!")
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password. {remaining} attempts remaining.")

if not success:
    print("Access denied. Too many failed attempts.")

# For loop with conditional processing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
        print(f"{num} is even")
    else:
        odd_count += 1
        print(f"{num} is odd")

print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")

# ========== ADVANCED BOOLEAN CONCEPTS ==========

# Short-circuit evaluation
def expensive_function():
    print("This function was called!")
    return True

# AND short-circuit: if first is False, second won't be evaluated
result1 = False and expensive_function()  # expensive_function() not called
print(f"AND result: {result1}")

# OR short-circuit: if first is True, second won't be evaluated  
result2 = True or expensive_function()  # expensive_function() not called
print(f"OR result: {result2}")

# Truthiness and falsiness
values = [0, 1, "", "hello", [], [1,2,3], None, True, False]

for value in values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")

# Using boolean expressions for default values
user_name = input("Enter username (or press Enter for default): ")
final_name = user_name or "Guest"  # Uses "Guest" if user_name is empty
print(f"Welcome, {final_name}!")

print("\n--- End of Lesson ---")
