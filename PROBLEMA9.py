# Optimización de funciones: Escribe un programa que encuentre el 
#mínimo o máximo de una función cuadrática mediante el cálculo de su 
#derivada.

def optimizacion_funcion_cuadratica(a, b, c):

    if a == 0:
        return None
    x_critico = -b / (2 * a)
    y_critico = a * x_critico**2 + b * x_critico + c

    if a > 0:
        return "Mínimo", (x_critico, y_critico)
    else:
        return "Máximo", (x_critico, y_critico)
