# 12. Palindrome Check & 13. Reverse the number
original = input("\nEnter a number: ")
reversed_val = original[::-1]
print(f"Reversed number: {reversed_val}")
print(f"Is it a Palindrome? {original == reversed_val}")

# 14. Multiplication Table
num = int(input("\nEnter number for Multiplication Table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 15 & 16. Largest and Smallest of n numbers
count = int(input("\nHow many numbers do you want to compare? "))
nums = []
for i in range(count):
    val = float(input(f"Enter number {i+1}: "))
    nums.append(val)

if nums:
    print(f"Largest: {max(nums)}")
    print(f"Smallest: {min(nums)}")