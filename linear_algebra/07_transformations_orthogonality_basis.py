import numpy as np

# Linear transformation
A = np.array([
    [2, 0],
    [0, 3]
])

v = np.array([1, 2])

transformed_v = A @ v
print("Linear transformation:", transformed_v)

# Orthogonality
u = np.array([1, 0])
w = np.array([0, 1])

dot_product = np.dot(u, w)
print("Dot product:", dot_product)
print("Are u and w orthogonal?", dot_product == 0)

# Linear independence
dependent_1 = np.array([1, 2])
dependent_2 = np.array([2, 4])

is_multiple = np.all(dependent_2 == 2 * dependent_1)

print("Vector 1:", dependent_1)
print("Vector 2:", dependent_2)
print("Are the vectors linearly dependent?", is_multiple)

# Basis of R²
basis_1 = np.array([1, 0])
basis_2 = np.array([0, 1])

print("Basis vector 1:", basis_1)
print("Basis vector 2:", basis_2)
print("These vectors form the standard basis of R².")

# Linear transformation: [2 6]
# Dot product: 0
# Are u and w orthogonal? True
# Vector 1: [1 2]
# Vector 2: [2 4]
# Are the vectors linearly dependent? True
# Basis vector 1: [1 0]
# Basis vector 2: [0 1]
# These vectors form the standard basis of R².
