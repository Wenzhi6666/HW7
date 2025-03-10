import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def PercentVaR(r, alpha):
    plt.hist(r, bins=50, alpha=0.7, color='blue', edgecolor='black')
    plt.title("distribution")
    plt.xlabel("returns")
    plt.ylabel("frequency")
    plt.show()
    out = np.abs(np.quantile(r, 1 - alpha)
    return out
