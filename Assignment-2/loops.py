n = int(input("Enter the value of n: "))

# 1. Natural numbers up to n
print("Natural numbers:", end=" ")
for i in range(1, n + 1):
    print(i, end=" ")

# 2. Even numbers up to n
print("\nEven numbers:", end=" ")
for i in range(2, n + 1, 2):
    print(i, end=" ")

# 3. Odd numbers up to n
print("\nOdd numbers:", end=" ")
for i in range(1, n + 1, 2):
    print(i, end=" ")

# 4. Sum of natural numbers up to n
print(f"\nSum of natural numbers: {sum(range(1, n + 1))}")

# 5. Sum of odd numbers up to n
print(f"Sum of odd numbers: {sum(i for i in range(1, n + 1) if i % 2 != 0)}")

# 6. Sum of even numbers up to n
print(f"Sum of even numbers: {sum(i for i in range(1, n + 1) if i % 2 == 0)}")

# 7. Natural numbers in reverse order
print("Natural numbers (Reverse):", end=" ")
for i in range(n, 0, -1):
    print(i, end=" ")