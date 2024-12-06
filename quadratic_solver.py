import math
with open("coefficients.txt", "r") as file:
    for line in file:
        a, b, c = map(float, line.split())
        discriminant = b**2 - 4 * a * c
        if discriminant >= 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f"Roots for {a}, {b}, {c}: {root1} and {root2}")
        else:
            print(f"No real roots for {a}, {b}, {c}")