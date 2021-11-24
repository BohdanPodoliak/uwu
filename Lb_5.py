import numpy as np 
from numpy import linalg

def gauss(a, b):
    n = len(b)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                
                lam = a[i,k]/a[k,k]
                a[i,k+1:n]= a[i,k+1:n] - lam*a[k,k+1:n] 
                b[i] = b[i] - lam*b[k]
    
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b 
print(gauss(np.matrix([[1,2, -1],[3,4, 1], [5, 1, -3]]), np.matrix([[-3], [1], [-2]])))