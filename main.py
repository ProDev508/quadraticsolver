import math


def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2


# Get user input
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Solve the quadratic equation
roots = solve_quadratic(a, b, c)

# Display the roots
root1, root2 = roots
print("Root 1:", root1)
print("Root 2:", root2)
