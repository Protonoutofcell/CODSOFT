def calculator():
    print("--- Simple Python Calculator ---")
    
    try:
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        choice = input("\nEnter choice (1/2/3/4): ")

        if choice == '1':
            result = num1 + num2
            operation = "+"
        elif choice == '2':
            result = num1 - num2
            operation = "-"
        elif choice == '3':
            result = num1 * num2
            operation = "*"
        elif choice == '4':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
            operation = "/"
        else:
            return "Invalid input! Please select a valid operation."

        return f"\nResult: {num1} {operation} {num2} = {result}"

    except ValueError:
        return "Invalid input! Please enter numerical values."

print(calculator())
