def calculator():
    print("Hey, Welcome to the Smart Calculator! Let's crunch some numbers!")
    
    
    number1 = float(input("Please, Enter the first(1st) number: "))
    number2 = float(input("please, Enter the second(2nd) number: "))
    
    print("Choose an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
   
    choice = input("\nNow, Please Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        result = number1 + number2
        operation = "+"
    elif choice == '2':
        result = number1 - number2
        operation = "-"
    elif choice == '3':
        result = number1 * number2
        operation = "*"
    elif choice == '4':
        if number2 != 0:
            result = number1 / number2
            operation = "/"
        else:
            result = "Sorry, It's undefined (division by zero!)"
            operation = "/"
    else:
        result = None

    if result is not None:
        print(f"\nCalculation: {number1} {operation} {number2} = {result}")
        print("Well done, you've Got it\nKeep it Up! 😎")
    else:
        print("\nOops! That's not a valid operation choice. Please try again!")

calculator()