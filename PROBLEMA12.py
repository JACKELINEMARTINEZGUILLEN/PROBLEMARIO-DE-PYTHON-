#Resolución de sistemas lineales: Implementa una función que resuelva 
#un sistema de ecuaciones lineales usando el método de eliminación de 
#Gauss.
import numpy as np

def gauss_eliminacion(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):

        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]
        
        Ab[i] = Ab[i] / Ab[i, i]
        
        for j in range(i + 1, n):
            Ab[j] = Ab[j] - Ab[i] * Ab[j, i]

     x = np.zeros(n)
     for i in range(n - 1, -1, -1):
         x[i] = Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])
    
     return x 
