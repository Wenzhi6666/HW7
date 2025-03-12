import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
  
    y2 = y / ppy   
    C = (couponRate * face)/ppy
    N = m * ppy
    time = np.arange(1, N+1)/ppy
    cashflows = np.full(N,C)
    cashflows[-1] += face  
    discountfactor = (1 + y2) ** (-time)
    pvcf = cashflows * discountfactor
    weightedpvcf = pvcf * time
    duration = np.sum(weightedpvcf) / np.sum(pvcf) 
    return duration
