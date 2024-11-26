#Cálculo numérico de integrales: Diseña una función para calcular la 
#integral definida de una función en un intervalo utilizando el método del 
#trapecio.
import numpy as np

def integral_definida_trapecio(f, a, b, n=1000):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * np.sum(y[1:] + y[:-1])
    return integral
