import numpy as np

v = np.array([1, 2, 3, 4, 5, 6])

print(f"Shape: {np.shape(v)}")

v2 = np.reshape(v, (2, 3))
print(f"Reshaped matrix:\n{v2}")

t = np.transpose(v2)
print(f"Transposed matrix:\n{t}")

print(f"Transposed shape: {np.shape(t)}")
