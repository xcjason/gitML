import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n, p = 10, 0.3
k = np.arange(21)
binomial = binom.pmf(k, n, p)
plt.plot(k, binomial, 'o-')
plt.show()