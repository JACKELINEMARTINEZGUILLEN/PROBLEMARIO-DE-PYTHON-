#Aproximación de derivadas: Implementa una función que calcule la 
#derivada de una función en un punto usando diferencias finitas.

def derivada_numerica(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)
