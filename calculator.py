def calculator():
    operand1 = input("Enter your first number: ")
    operand2 = input("Enter your second number: ")

    if operand1.isdigit() and operand2.isdigit():
        operand1 = int(operand1)
        operand2 = int(operand2)

        print("Press '+' for Addition")
        print("Press '-' for Subtraction")
        print("Press '*' for Multiplication")
        print("Press '/' for Division")
        print("Press '%' for Modulus")
        print("Press '**' for Power")

        operator = input("Enter your operator: ")

        if operator == "+":
            print(operand1 + operand2)
        elif operator == "-":
            print(operand1 - operand2)
        elif operator == "*":
            print(operand1 * operand2)
        elif operator == "/":
            if operand2 != 0:
                print(operand1 / operand2)
            else:
                print("Cannot divide by zero.")
        elif operator == "%":
            print(operand1 % operand2)
        elif operator == "**":
            print(operand1 ** operand2)
        else:
            print("Invalid operator")
    else:
        print("Invalid input. Please enter valid numbers.")
        calculator()

calculator()
