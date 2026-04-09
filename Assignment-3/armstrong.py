# Program to check if a number is an Armstrong number
num = int(input("Enter a number: "))
order = len(str(num)) # Find number of digits
temp = num
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** order
    temp //= 10

if num == sum_val:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")