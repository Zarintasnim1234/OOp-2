num = int(input("Enter a number to display its multiplication table: "))


print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")