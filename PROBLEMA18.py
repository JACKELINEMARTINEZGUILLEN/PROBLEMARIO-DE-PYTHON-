#Factorización optimizada: Diseña una función para descomponer un 
#número en sus factores primos de forma eficiente.
from collections import defaultdict

def factorizacion_prima(n):
    factores = defaultdict(int)
    while n % 2 == 0:
        factores[2] += 1
        n //= 2
    while n % 3 == 0:
        factores[3] += 1
        n //= 3
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        while n % i == 0:
            factores[i] += 1
            n //= i
        while n % (i + 2) == 0:
            factores[i + 2] += 1
            n //= (i + 2)

    if n > 1:
        factores[n] += 1 
    
    return dict(factores)
