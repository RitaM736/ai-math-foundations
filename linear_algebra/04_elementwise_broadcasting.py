import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Element-wise operations
print("A + B:", A + B)
print("A - B:", A - B)
print("A * B:", A * B)
print("A / B:", A / B)

# Broadcasting with a scalar
print("A * 10:", A * 10)
print("A + 10:", A + 10)

# Broadcasting with a vector
C = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

D = np.array([10, 20, 30])

print("C + D:")
print(C + D)



A + B: [5 7 9]
A - B: [-3 -3 -3]
A * B: [ 4 10 18]
A / B: [0.25 0.4  0.5 ]

A * 10: [10 20 30]
A + 10: [11 12 13]

C + D:
[[11 22 33]
 [14 25 36]]
