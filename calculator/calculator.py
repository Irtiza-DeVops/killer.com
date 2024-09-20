def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

print("****************************************")
print("          WELCOME TO THE CALCULATOR    ")
print("****************************************")

while True:
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (÷)")
    print("5. Exit")
    print("****************************************")

    operation = input("Enter the operation (1/2/3/4/5): ")

    if operation in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == '1':
            result = add(num1, num2)
            print(f"\n✨ The result of {num1} + {num2} = {result} ✨")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"\n✨ The result of {num1} - {num2} = {result} ✨")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"\n✨ The result of {num1} * {num2} = {result} ✨")
        elif operation == '4':
            result = divide(num1, num2)
            print(f"\n✨ The result of {num1} ÷ {num2} = {result} ✨")
    elif operation == '5':
        print("****************************************")
        print("           Exiting the calculator.     ")
        print("           Thank you for using!        ")
        print("****************************************")
        break
    else:
        print("\n❌ Invalid operation selected! Please try again. ❌")
