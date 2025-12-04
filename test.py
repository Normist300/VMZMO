import numpy as np

b_grid = np.arange(500, 601)
prior = np.ones_like(b_grid) / len(b_grid)
print(prior)