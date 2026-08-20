import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(f"Shape: {np.shape(A)}")
print(f"Dimensions: {np.ndim(A)}")
print(f"Size: {np.size(A)}")

print(f"Mean of the whole matrix: {np.mean(A)}")

print(f"Mean by columns: {np.mean(A, axis=0)}")
print(f"Mean by rows: {np.mean(A, axis=1)}")

print(f"Min: {np.min(A)}")
print(f"Max: {np.max(A)}")
