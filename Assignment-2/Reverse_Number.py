# Program to reverse a number using math logic
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(f"Reversed Number: {reverse}")