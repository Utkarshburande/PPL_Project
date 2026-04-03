# --- Lab Assignment 2 ---
# Program to grade steel based on Hardness, Carbon content, and Tensile strength

# 1. Input values from the user
hardness = float(input("Enter Hardness of steel: "))
carbon_content = float(input("Enter Carbon content: "))
tensile_strength = float(input("Enter Tensile strength: "))

# 2. Check the three specific conditions
cond1 = hardness > 50
cond2 = carbon_content < 0.7
cond3 = tensile_strength > 5600

# 3. Determine Grade based on conditions
if cond1 and cond2 and cond3:
    grade = 10
elif cond1 and cond2:
    grade = 9
elif cond2 and cond3:
    grade = 8
elif cond1 and cond3:
    grade = 7
elif cond1 or cond2 or cond3:
    # If only one condition (any of them) is met
    grade = 6
else:
    # If none of the conditions are met
    grade = 5

# 4. Output the result
print("-" * 30)
print(f"Steel Quality Grade: {grade}")
print("-" * 30)