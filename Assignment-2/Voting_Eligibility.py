# Program to check voting eligibility
age = int(input("Enter the age of the person: "))

if age >= 18:
    print("The person is eligible to vote in India.")
else:
    print(f"The person is not eligible to vote. Wait {18 - age} more year(s).")