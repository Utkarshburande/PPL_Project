# Program to check if a number is even or odd
number = int(input("Enter a number: "))

# A number is even if it is divisible by 2 with no remainder
if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")