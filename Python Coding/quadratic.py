import math


def solve_quadratic(a, b, c):
    
    discriminant = b**2 - 4*a*c

   
    if discriminant > 0:
        
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"The equation has two real roots: {root1} and {root2}"
    elif discriminant == 0:
        
        root = -b / (2 * a)
        return f"The equation has one real root: {root}"
    else:
        
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"The equation has two complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i"


print("For the quadratic equation ax^2 + bx + c = 0")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


if a == 0:
    print("This is not a quadratic equation (a cannot be 0).")
else:
    result = solve_quadratic(a, b, c)
    print(result)