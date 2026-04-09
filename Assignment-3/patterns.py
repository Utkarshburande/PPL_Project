# --- Pattern A: Incremental numbers ---
print("Pattern A:")
val = 1
for i in range(1, 5):
    for j in range(i):
        print(val, end=" ")
        val += 1
    print()

# --- Pattern B: Star Triangle ---
print("\nPattern B:")
for i in range(1, 6):
    print("*" * i)

# --- Pattern C: Repeating Row Numbers ---
print("\nPattern C:")
for i in range(1, 6):
    for j in range(6 - i):
        print(i, end=" ")
    print()

# --- Pattern D: Descending Rows ---
print("\nPattern D:")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# --- Pattern E: Right-Aligned Numbers ---
print("\nPattern E:")
for i in range(1, 6):
    # Printing spaces
    print("  " * (5 - i), end="")
    # Printing numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# --- Pattern F: Star Pyramid ---
print("\nPattern F:")
for i in range(1, 6):
    # Spaces for alignment
    print(" " * (5 - i), end="")
    # Stars (Odd numbers: 1, 3, 5, 7, 9)
    print("*" * (2 * i - 1))