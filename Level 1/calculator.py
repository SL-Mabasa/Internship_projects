def calculator(num1, num2, operation):
    file = open("equations.txt", "a")
    if operation == "+":
        result = num1 + num2
        written_result = (f"{num1} {operation} {num2} = {result}\n")
        file.write(written_result)
        file.close()
        return print(f'\n{written_result}\n')
    elif operation == "-":
        result = num1 - num2
        written_result = (f"{num1} {operation} {num2} = {result}\n")
        file.write(written_result)
        file.close()
        return print(f'\n{written_result}\n')
    elif operation == "*":
        result = num1 * num2
        written_result = (f"{num1} {operation} {num2} = {result}\n")
        file.write(written_result)
        file.close()
        return print(f'\n{written_result}\n')
    elif operation == "/":
        try:
            result = num1 / num2
            written_result = (f"{num1} {operation} {num2} = {result}\n")
            file.write(written_result)
            file.close()
            return print(f'\n{written_result}\n')
        except ZeroDivisionError:
            print("\nYou cannot divide by zero.\n")
            


print("\nThis program calculates two numbers you choose based on the operator you choose.\n")

while True:
    choice = input("Would you like to: \n1. Create new equation \n2. View existing calculations \n3. End program \n-> ")
    if choice == '1':
        while True:
            try:
                number_1 = int(input("\nEnter the first integer number: "))
                break
            except ValueError:
                print("\nPlease enter integer(whole number) value.\n")
          
        while True:
            try:
                number_2 = int(input("\nEnter the second integer number: "))
                break
            except ValueError:
                print("\nPlease enter integer(whole number) value.\n")

        while True:
            operator_choice = str(input("\nPlease enter operator of choice. Enter (+) for addition, (-) for subtraction, (*) for multiplication or (/) for division \n: "))
           
            if operator_choice == "+":
                calculator(number_1, number_2, operator_choice)
                break
            elif operator_choice == "-":
                calculator(number_1, number_2, operator_choice)
                break
            elif operator_choice == "*":
                calculator(number_1, number_2, operator_choice)
                break
            elif operator_choice == "/":
                calculator(number_1, number_2, operator_choice)
                break
            else:
                print(f"\n{operator_choice} is not an operator. Please only enter + , - , * or / as operator.")
    
    elif choice == '2':
        try:
            file = open("equations.txt")
            print(f'\n{file.read()}\n')
            file.close()
        except FileNotFoundError:
            print("\nThere are no previous or existing equations. Please try and create a new equation instead.\n")

    elif choice == '3':
        print("\nHave a Good day!!\n")
        exit()
    
    else:
        print("Invalid choice. Pick Option 1 - 3")