def calculator():
    while True:
        print("\n--- Calculator ---")
        print("1. Enter numbers and calculate")
        print("2. Exit")
        menu_choice = input("Choose an option : ")

        if menu_choice == '1':
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                print("\nSelect an operation:")
                print("1. Addition (+)")
                print("2. Subtraction (-)")
                print("3. Multiplication (*)")
                print("4. Division (/)")
                operation = input("Enter your choice : ")

                if operation == '1':
                    result = num1 + num2
                    print(f"The result of {num1} + {num2} is {result}.")
                elif operation == '2':
                    result = num1 - num2
                    print(f"The result of {num1} - {num2} is {result}.")
                elif operation == '3':
                    result = num1 * num2
                    print(f"The result of {num1} * {num2} is {result}.")
                elif operation == '4':
                    if num2 != 0:
                        result = num1 / num2
                        print(f"The result of {num1} / {num2} is {result}.")
                    else:
                        print("Error: Division by zero is not allowed.")
                else:
                    print("Invalid operation choice! Please try again.")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        elif menu_choice == '2':
            print("Thank you for using the calculator.")
            break
        else:
            print("Invalid choice! Please select a valid menu option.")

calculator()