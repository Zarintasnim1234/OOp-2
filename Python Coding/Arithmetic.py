def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x / y


print("Select an arithmetic operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


choice = input("Enter choice (1/2/3/4): ")


if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"The result of addition is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of subtraction is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of multiplication is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result of division is: {divide(num1, num2)}")
else:
    print("Invalid input! Please select a valid operation.")