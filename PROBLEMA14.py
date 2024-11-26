#Multiplicación de matrices grandes: Implementa un algoritmo para 
#multiplicar dos matrices dispersas eficientemente.

from scipy.sparse import csr_matrix

def multiplicacion_dispersa(A_data, A_indices, A_indptr, B_data, B_indices, B_indptr, shape):
    A = csr_matrix((A_data, A_indices, A_indptr), shape=shape)
    B = csr_matrix((B_data, B_indices, B_indptr), shape=shape)

    C = A.dot(B)
    return C

