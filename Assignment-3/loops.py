# Program to print a statement 20 times using a while loop
count = 1
while count <= 20:
    print(f"{count}. Hello Students")
    count += 1

    # Program to calculate the sum of numbers from 1 to a given number
n = int(input("Enter a number: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"The sum of all numbers from 1 to {n} is: {total_sum}")