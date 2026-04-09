# 8. Fibonacci Series up to n
n = int(input("\nEnter range for Fibonacci: "))
a, b = 0, 1
print("Fibonacci series:", end=" ")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b

# 9. Factorial of a number
num = int(input("\n\nEnter number for factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")

# 10. Check if a number is Prime
num = int(input("Enter number to check prime: "))
is_prime = True
if num < 2:
    is_prime = False
else:
    # Check divisibility up to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
print(f"{num} is Prime: {is_prime}")

# 11. Sum of digits
num = int(input("Enter number to find sum of digits: "))
digit_sum = sum(int(digit) for digit in str(abs(num)))
print(f"Sum of digits: {digit_sum}")