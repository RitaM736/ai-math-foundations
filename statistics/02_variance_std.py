import numpy as np

scores = np.array([60, 70, 70, 80, 90])

# Mean
mean = np.mean(scores)
print("Mean:", mean)

# Variance
variance = np.var(scores)
print("Variance:", variance)

# Standard deviation
std = np.std(scores)
print("Standard deviation:", std)

# Difference of each score from the mean
differences = scores - mean
print("Differences from mean:", differences)

# Squared differences
squared_differences = differences ** 2
print("Squared differences:", squared_differences)

# Mean: 74.0
# Variance: 104.0
# Standard deviation: 10.198...
# Differences from mean: [-14.  -4.  -4.   6.  16.]
# Squared differences: [196.  16.  16.  36. 256.]
