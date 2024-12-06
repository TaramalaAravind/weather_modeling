import math
a, b, c = 1, -3, 2
discriminant = b**2 - 4*a*c
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots are: {root1} and {root2}")
else:
    print("No real roots")
