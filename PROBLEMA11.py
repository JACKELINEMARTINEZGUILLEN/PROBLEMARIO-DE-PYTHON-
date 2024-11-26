#Tangente a una curva: Dada una función y un punto, calcula la ecuación 
#de la recta tangente en ese punto.

def ecuacion_recta_tangente(f, x0):
    m = derivada_numerica(f, x0)
    y0 = f(x0)
    b = y0 - m * x0
    return lambda x: m * x + b
