import math

# 1. Circle Calculations
radius = float(input("Enter the radius of the circle: "))
area_circle = math.pi * radius**2
circumference = 2 * math.pi * radius

# 2. Cube Calculation
side = float(input("Enter the side length of the cube: "))
volume_cube = side**3

# 3. Cone Calculation
h_cone = float(input("Enter the height of the cone: "))
r_cone = float(input("Enter the radius of the cone base: "))
volume_cone = (1/3) * math.pi * (r_cone**2) * h_cone

# Results
print("\n--- Geometric Results ---")
print(f"Area of Circle: {area_circle:.2f}")
print(f"Circumference of Circle: {circumference:.2f}")
print(f"Volume of Cube: {volume_cube:.2f}")
print(f"Volume of Cone: {volume_cone:.2f}")