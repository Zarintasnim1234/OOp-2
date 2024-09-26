def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def display_fibonacci_sequence(count):
    print("Fibonacci sequence:")
    for i in range(count):
        print(fibonacci(i), end=" ")


if __name__ == "__main__":
    n_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
    display_fibonacci_sequence(n_terms)