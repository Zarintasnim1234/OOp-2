def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number


start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print(f"Armstrong numbers between {start} and {end} are:")


for num in range(start, end + 1):
    if is_armstrong(num):
        print(num)