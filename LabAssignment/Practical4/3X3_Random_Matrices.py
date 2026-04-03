import numpy as np

# a) Generate a 4x4 identity matrix
identity_matrix = np.eye(4)
print("--- 4x4 Identity Matrix ---")
print(identity_matrix)

# b) Generate two 3x3 matrices with random integers (1 to 9)
# random.randint(low, high, size)
matrix_a = np.random.randint(1, 10, size=(3, 3))
matrix_b = np.random.randint(1, 10, size=(3, 3))

print("\n--- Matrix A (3x3) ---")
print(matrix_a)
print("\n--- Matrix B (3x3) ---")
print(matrix_b)

# Perform Matrix Addition
add_result = matrix_a + matrix_b
print("\n--- Matrix Addition (A + B) ---")
print(add_result)

# Perform Matrix Multiplication (Dot Product)
mult_result = np.dot(matrix_a, matrix_b)
# Alternatively, you can use the @ operator: matrix_a @ matrix_b
print("\n--- Matrix Multiplication (A * B) ---")
print(mult_result)