import numpy as np

A = np.array([3, 4])
B = np.array([6, 8])
C = np.array([4, 3])

# 1. L1 norm of A
l1_A = np.linalg.norm(A, ord=1)
print("L1 norm of A:", l1_A)

# 2. L2 norm of A
l2_A = np.linalg.norm(A, ord=2)
print("L2 norm of A:", l2_A)

# 3. Euclidean distance between A and B
distance_AB = np.linalg.norm(A - B)
print("Euclidean distance A-B:", distance_AB)

# 4. Cosine similarity between A and B
cosine_AB = np.dot(A, B) / (
    np.linalg.norm(A) * np.linalg.norm(B)
)
print("Cosine similarity A-B:", cosine_AB)

# 5. Cosine similarity between A and C
cosine_AC = np.dot(A, C) / (
    np.linalg.norm(A) * np.linalg.norm(C)
)
print("Cosine similarity A-C:", cosine_AC)
