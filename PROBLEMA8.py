#Aproximación de derivadas usando diferencias finitas

def derivada_numerica(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)
