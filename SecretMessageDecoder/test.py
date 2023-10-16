import numpy as np

# Define matrices A and C
A = np.array([[2, 1], [1, 3]])
C = np.array([[5, 7], [8, 9]])

# Calculate the inverse of matrix A
A_inv = np.linalg.inv(A)

# Find matrix B
B = np.dot(A_inv, C)

print(B)
