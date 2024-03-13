import math

import numpy as np

numpy_score = np.array([20, 18, 16])
numpy_score_weight = np.array([.1, .3, .6])

print(numpy_score * numpy_score_weight)
print(math.floor(np.sum(numpy_score * numpy_score_weight) * 10) / 10)
print(20 * .1 + 18 * .3 + 16 * .6)
