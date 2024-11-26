#Resolución de sistemas lineales: Implementa una función que resuelva 
#un sistema de ecuaciones lineales usando el método de eliminación de 
#Gauss.
import numpy as np

def gauss_eliminacion(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)])
  
