import numpy as np

def Forecast_nPeriod(vec, tmat, n):
    out = np.eye(tmat.shape[0]) 
    for _ in range(n):
        out = np.dot(out, tmat)  
    out = np.dot(vec, out)
    return out
