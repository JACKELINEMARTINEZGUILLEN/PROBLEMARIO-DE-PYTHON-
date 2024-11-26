#Determinante de una matriz: Crea una función que calcule el 
#determinante de matrices de hasta 4x4.
from scipy.sparse.linalg import spsolve

def determinante_matriz(M):
    if M.shape[0] != M.shape[1] or M.shape[0] > 4:
        raise ValueError("La matriz debe ser cuadrada y de tamaño máximo 4x4.")
  
    return round(np.linalg.det(M), 5)
    
