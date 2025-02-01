def arithmetic_operation():
    # Input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /, %, **, //): ")

    # Perform the operation using match-case
    match operator:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error! Division by zero is not allowed."
        case "%":
            if num2 != 0:
                result = num1 % num2
            else:
                return "Error! Division by zero is not allowed."
        case "**":
            result = num1 ** num2
        case "//":
            if num2 != 0:
                result = num1 // num2
            else:
                return "Error! Division by zero is not allowed."
        case _:
            return "Invalid operator! Please use +, -, *, /, %, **, or //."

    return f"The result of {num1} {operator} {num2} is: {result}"

# Call the function and print the result
print(arithmetic_operation())
