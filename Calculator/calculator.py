# Define function for basic operations
def sum(x, y):
    return x + y

def multiplication(x, y):
    return x * y

def subtraction(x, y):
    return x - y

def division(x, y):
    if y == 0:
        return "undefined"
    else:
        return x / y

def calculator():
    while True:
        # Get numbers and operation from the user
        num1 = float(input("Enter the first number : "))
        num2 = float(input("Enter the second number : "))
        choice = input("""Please choose one of the four basic math options: 
                        1 = add 
                        2 = multiplication
                        3 = subtract
                        4 = divide 
                        """)

        # Perform the operation and store the result
        if choice == '1':
            result = sum(num1, num2)
        elif choice == '2':
            result = multiplication(num1, num2)
        elif choice == '3':
            result = subtraction(num1, num2)
        elif choice == '4':
            result = division(num1, num2)
        else:
            print("Invalid operation!")
            continue

        print(f"Result = {result}")

        # Ask the user if they want to perform another operation on the result
        while True:
            again = input("Do you want to perform another operation on the result? Enter yes or no: ")
            if again.lower() == "yes":
                num1 = result
                choice = input("""Please choose one of the four basic math options: 
                                1 = add 
                                2 = multiplication
                                3 = subtract
                                4 = divide 
                                """)
                num2 = float(input("Please enter number 2: "))

                # Perform the operation and update the result
                if choice == '1':
                    result = sum(num1, num2)
                elif choice == '2':
                    result = multiplication(num1, num2)
                elif choice == '3':
                    result = subtraction(num1, num2)
                elif choice == '4':
                    result = division(num1, num2)
                else:
                    print("Invalid operation! Please try again.")
                    continue

                print(f"Result = {result}")

            elif again.lower() == "no":
                break
            else:
                print("Please enter yes or no")
                continue

        # Ask the user if they want to perform a new calculation
        another_calc = input("Do you want to perform a new calculation? yes or no: ")
        if another_calc.lower() == "no":
            break

calculator()

     
     