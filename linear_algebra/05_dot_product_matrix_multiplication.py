import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

M = np.array([
    [1, 2],
    [3, 4]
])

N = np.array([
    [5, 6],
    [7, 8]
])

# 1. Calculate the dot product using np.dot()
dot_result = np.dot(A, B)
print("Dot product using np.dot():", dot_result)

# 2. Calculate the dot product using @
dot_at_result = A @ B
print("Dot product using @:", dot_at_result)

# 3. Verify both results are equal
print("Results are equal:", dot_result == dot_at_result)

# 4. Print A.shape and B.shape
print("A shape:", A.shape)
print("B shape:", B.shape)

# 5. Calculate M @ N
matrix_result = M @ N
print("M @ N:")
print(matrix_result)

# 6. Print M.shape, N.shape, and (M @ N).shape
print("M shape:", M.shape)
print("N shape:", N.shape)
print("M @ N shape:", matrix_result.shape)
