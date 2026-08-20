import numpy as np
from sklearn.decomposition import PCA

# --------------------------------------------------
# 1. Eigenvalues and Eigenvectors
# --------------------------------------------------

A = np.array([
    [2, 0],
    [0, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)


# --------------------------------------------------
# 2. Verify an Eigenvector
# --------------------------------------------------

v = eigenvectors[:, 0]
lambda_value = eigenvalues[0]

print("\nVerification of eigenvector:")
print("Av:", A @ v)
print("lambda * v:", lambda_value * v)
print("Valid:", np.allclose(A @ v, lambda_value * v))


# --------------------------------------------------
# 3. Matrix Inverse
# --------------------------------------------------

A_inv = np.linalg.inv(A)

print("\nInverse of A:")
print(A_inv)


# --------------------------------------------------
# 4. Determinant
# --------------------------------------------------

det_A = np.linalg.det(A)

print("\nDeterminant of A:")
print(det_A)


# --------------------------------------------------
# 5. Matrix Rank
# --------------------------------------------------

rank_A = np.linalg.matrix_rank(A)

print("\nRank of A:")
print(rank_A)


# --------------------------------------------------
# 6. SVD
# --------------------------------------------------

X = np.array([
    [2, 1],
    [3, 2],
    [4, 3],
    [5, 4],
    [6, 5]
])

U, S, Vt = np.linalg.svd(X)

print("\nSVD - U:")
print(U)

print("\nSVD - Singular Values:")
print(S)

print("\nSVD - Vt:")
print(Vt)


# --------------------------------------------------
# 7. PCA
# --------------------------------------------------

pca = PCA(n_components=1)

X_reduced = pca.fit_transform(X)

print("\nPCA:")
print("Original shape:", X.shape)
print("Reduced shape:", X_reduced.shape)

print("\nReduced data:")
print(X_reduced)

print("\nExplained variance ratio:")
print(pca.explained_variance_ratio_)
