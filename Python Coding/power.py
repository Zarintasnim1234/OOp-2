def power(base, exponent):
    if exponent < 0:
        return 1 / power(base, -exponent)  
    elif exponent == 0:
        return 1  
    else:
        return base * power(base, exponent - 1) 

#
if __name__ == "__main__":
    base = float(input("Enter the base number: "))
    exponent = int(input("Enter the exponent (positive or negative): "))
    result = power(base, exponent)
    print(f"{base} raised to the power of {exponent} is: {result}")