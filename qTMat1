import numpy as np

def TMAT1(vec1, vec2):
    unistates = np.unique(np.concatenate((vec1, vec2)))
    n = len(unistates)  
    mat = np.zeros((n, n))
    for i, state_from in enumerate(unistates):
        mask = vec1 == state_from  
        transitions = vec2[mask]        
        for j, state_to in enumerate(unistates):
            mat[i, j] = np.sum(transitions == state_to
    rowsums = mat.sum(axis=1, keepdims=True)
    mat = np.divide(mat, rowsums, where=rowsums != 0)  
    return mat
