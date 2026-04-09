import math

# Program to find the area of a circle
radius = float(input("Enter the radius of the circle: "))

# Formula: Area = π * r^2
area = math.pi * (radius ** 2)

print(f"The area of the circle with radius {radius} is {area:.2f}")