#Posición en Fibonacci: Escribe una función que determine si un número 
#dado pertenece a la serie de Fibonacci. Si pertenece, devuelve su posición.

def posicion_en_fibonacci(num):
    
    a, b = 0, 1
    pos = 1
    while a < num:
        a, b = b, a + b
        pos += 1
    if a == num:
        return pos
    return -1 
