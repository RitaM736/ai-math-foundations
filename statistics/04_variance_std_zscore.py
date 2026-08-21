```python
import numpy as np

# Scores
scores = np.array([50, 60, 70, 80, 90, 100])

# --------------------------------------------------
# 1. Mean
# --------------------------------------------------

mean = np.mean(scores)

print("Mean:", mean)


# --------------------------------------------------
# 2. Differences from the mean
# --------------------------------------------------

differences = scores - mean

print("Differences from mean:", differences)


# --------------------------------------------------
# 3. Squared differences
# --------------------------------------------------

squared_differences = differences ** 2

print("Squared differences:", squared_differences)


# --------------------------------------------------
# 4. Variance
# --------------------------------------------------

variance = np.var(scores)

print("Variance:", variance)


# --------------------------------------------------
# 5. Standard deviation
# --------------------------------------------------

std = np.std(scores)

print("Standard deviation:", std)


# --------------------------------------------------
# 6. Z-scores
# --------------------------------------------------

z_scores = (scores - mean) / std

print("Z-scores:", z_scores)


# --------------------------------------------------
# 7. Z-score of a specific value
# --------------------------------------------------

score = 90

z_score_90 = (score - mean) / std

print("Z-score of 90:", z_score_90)
```

### Expected output

```text
Mean: 75.0

Differences from mean:
[-25. -15.  -5.   5.  15.  25.]

Squared differences:
[625. 225.  25.  25. 225. 625.]

Variance:
291.6666666666667

Standard deviation:
17.07825127659933

Z-scores:
[-1.46385011 -0.87831007 -0.29277002  0.29277002  0.87831007  1.46385011]

Z-score of 90:
0.8783100656536799

