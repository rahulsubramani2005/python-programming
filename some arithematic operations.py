# Define the arithmetic operations as functions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def remainder(a, b):
    return a % b

def floor_division(a, b):
    return a // b

def exponentiation(a, b):
    return a ** b

# Input values
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Display options for arithmetic operations
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder")
print("6. Floor Division")
print("7. Exponentiation")

# Take the user's choice
choice = int(input("Please enter your choice: "))

# Create a dictionary to simulate a switch-case
switch_case = {
    1: addition,
    2: subtraction,
    3: multiplication,
    4: division,
    5: remainder,
    6: floor_division,
    7: exponentiation
}

# Perform the operation based on the user's choice using the dictionary
if choice in switch_case:
    result = switch_case[choice](a, b)
    print(result)
else:
    print("Invalid choice. Please enter a number between 1 and 7.")
