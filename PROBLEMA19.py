#Número de caminos: Calcula el número de caminos posibles en una 
#cuadrícula NxN, moviéndose solo hacia la derecha o hacia abajo

def numero_caminos(N):
  
    return math.comb(2 * N, N)
