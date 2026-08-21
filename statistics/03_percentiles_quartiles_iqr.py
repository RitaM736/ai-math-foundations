import numpy as np

scores = np.array([
    50, 55, 60, 65, 70,
    75, 80, 85, 90, 95
])

# 1. 25th percentile (Q1)
q1 = np.percentile(scores, 25)
print("Q1:", q1)

# 2. 50th percentile (Q2 / Median)
q2 = np.percentile(scores, 50)
print("Q2:", q2)

# 3. 75th percentile (Q3)
q3 = np.percentile(scores, 75)
print("Q3:", q3)

# 4. Interquartile Range
iqr = q3 - q1
print("IQR:", iqr)


# Q1: 61.25
# Q2: 72.5
# Q3: 83.75
# IQR: 22.5
