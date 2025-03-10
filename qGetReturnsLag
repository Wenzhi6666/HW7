import numpy as np

def getReturns(pricevec, lag=1):  
    pricevec = np.array(pricevec, dtype=np.float64)
    returns = (pricevec[lag:] - pricevec[:-lag]) / pricevec[:-lag]
    return returns
