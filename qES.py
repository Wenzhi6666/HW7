import numpy as np

def ES(losses, alpha=None, VaR=None):
   if VaR is not None:
        out = losses[losses > VaR].mean()
    else:
        VaR = np.percentile(losses, 100 * (1-alpha))
        out = losses[losses > VaR].mean() 
    return out
