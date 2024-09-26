def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

terms = int(input("Enter the number of terms in the Fibonacci sequence: "))


if terms <= 0:
    print("Please enter a positive integer.")
else:
    
    print(f"Fibonacci sequence with {terms} terms:")
    print(fibonacci(terms))