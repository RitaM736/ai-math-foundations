import numpy as np

scores = np.array([10, 12, 13, 14, 15, 16, 17, 50])

# Q1 and Q3
q1 = np.percentile(scores, 25)
q3 = np.percentile(scores, 75)

# IQR
iqr = q3 - q1

# Outlier boundaries
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Find all outliers
outliers = scores[
    (scores < lower_bound) |
    (scores > upper_bound)
]

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower boundary:", lower_bound)
print("Upper boundary:", upper_bound)
print("Outliers:", outliers)
# Q1: 12.75 Q3: 16.25 IQR: 3.5 Lower boundary: 7.5 Upper boundary: 21.5 Outliers: [50]
