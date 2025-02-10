# Input from user
char = input("Enter a character: ")

# Check if the character is uppercase, lowercase, digit, or other
if char.isupper():
    print("Uppercase letter")
elif char.islower():
    print("Lowercase letter")
elif char.isdigit():
    print("Digit")
else:
    print("Other character")
