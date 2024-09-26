def factorial(n):
    if n < 0:
        return "Error! Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    number = int(input("Enter a non-negative integer to find its factorial: "))
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")