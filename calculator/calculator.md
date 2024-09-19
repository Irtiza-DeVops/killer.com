Here’s a Markdown file explaining the updated calculator code with attractive print statements. You can copy and paste this into a `.md` file.

```markdown
# Simple Calculator Code Explanation

This document explains the code for a simple calculator that performs basic arithmetic operations with attractive print statements.

```python
def add(x, y):
    return x + y
```
- **Function Definition**: This defines a function named `add` that takes two parameters, `x` and `y`.
- **Return Statement**: It returns the sum of `x` and `y`.

```python
def subtract(x, y):
    return x - y
```
- **Function Definition**: Defines a function `subtract` that takes two parameters.
- **Return Statement**: It returns the result of `x` minus `y`.

```python
def multiply(x, y):
    return x * y
```
- **Function Definition**: Defines a function `multiply` to multiply two numbers.
- **Return Statement**: It returns the product of `x` and `y`.

```python
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y
```
- **Function Definition**: Defines a function `divide` to divide two numbers.
- **Zero Check**: If `y` is zero, it returns an error message to avoid division by zero.
- **Return Statement**: If `y` is not zero, it returns the result of `x` divided by `y`.

```python
print("****************************************")
print("          WELCOME TO THE CALCULATOR    ")
print("****************************************")
```
- **Print Statements**: Displays a welcome message within a decorative border to make it visually appealing.

```python
while True:
```
- **Infinite Loop**: Starts a loop that will continue until explicitly broken.

```python
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Exit")
    print("****************************************")
```
- **Print Statements**: Displays the menu options for the user to choose from, along with a decorative border.

```python
    operation = input("Enter the operation (1/2/3/4/5): ")
```
- **Input Statement**: Prompts the user to enter their choice of operation and stores it in the variable `operation`.

```python
    if operation in ['1', '2', '3', '4']:
```
- **Condition Check**: Checks if the entered operation is valid (1 to 4).

```python
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
```
- **Input Statements**: Prompts the user to enter two numbers, converting them to floats for arithmetic operations.

```python
        if operation == '1':
            result = add(num1, num2)
            print(f"\n✨ The result of {num1} + {num2} = {result} ✨")
```
- **Addition Operation**: If the user chose addition, it calls the `add` function and prints the result with decorative emojis.

```python
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"\n✨ The result of {num1} - {num2} = {result} ✨")
```
- **Subtraction Operation**: If the user chose subtraction, it calls the `subtract` function and prints the result with decorative emojis.

```python
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"\n✨ The result of {num1} × {num2} = {result} ✨")
```
- **Multiplication Operation**: If the user chose multiplication, it calls the `multiply` function and prints the result with decorative emojis.

```python
        elif operation == '4':
            result = divide(num1, num2)
            print(f"\n✨ The result of {num1} ÷ {num2} = {result} ✨")
```
- **Division Operation**: If the user chose division, it calls the `divide` function and prints the result with decorative emojis.

```python
    elif operation == '5':
        print("****************************************")
        print("           Exiting the calculator.     ")
        print("           Thank you for using!        ")
        print("****************************************")
        break
```
- **Exit Option**: If the user chooses to exit, it prints a goodbye message and breaks the loop with decorative borders.

```python
    else:
        print("\n❌ Invalid operation selected! Please try again. ❌")
```
- **Invalid Operation Handling**: If the entered operation is not valid, it prompts the user to try again with an error emoji.
```

