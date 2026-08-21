import numpy as np
from statistics import mode

scores = np.array([65, 70, 72, 75, 75, 80, 82, 90, 95])

print("Number of observations:", scores.size)
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Mode:", mode(scores))
print("Minimum:", scores.min())
print("Maximum:", scores.max())
print("Range:", scores.max() - scores.min())
