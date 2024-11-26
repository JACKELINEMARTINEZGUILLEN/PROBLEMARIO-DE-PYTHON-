# Autovalores y autovectores: Escribe un programa para calcular los 
#autovalores de una matriz 2x2.


def autovalores_autovectores(A):
    if A.shape != (2, 2):
        raise ValueError("La matriz debe ser de 2x2.")
    
    autovalores, autovectores = np.linalg.eig(A)
    return autovalores, autovectores

