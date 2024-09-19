while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue
    
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Choose an operation (1/2/3/4) or type 'exit' to quit: ").strip()
    
    if operation.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    
    if operation == '1':
        result = num1 + num2
    elif operation == '2':
        result = num1 - num2
    elif operation == '3':
        result = num1 * num2
    elif operation == '4':
        result = num1 / num2 if num2 != 0 else "Error! Division by zero."
    else:
        result = "Invalid operation choice."
    
    print(f"The result is: {result}")
