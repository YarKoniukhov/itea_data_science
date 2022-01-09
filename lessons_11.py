import numpy as np
import sklearn


np.random.seed(42)
x = np.random.normal(0, 5, 100)
y = 50 + 2 * x + np.random.normal(0, 2, len(x))

print(x, y)