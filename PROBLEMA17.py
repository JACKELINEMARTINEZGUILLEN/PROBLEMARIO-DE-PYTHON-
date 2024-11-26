#TEORIA DE NUMEROS Y MATEMATICAS DISCRETAS
#Números amigables: Escribe un programa para determinar si dos 
#números dados son amigables (la suma de los divisores de uno es igual al 
#otro y viceversa).
import math

def divisores_propios(n):
    divisores = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisores.append(i)
            if i != n // i:  
                divisores.append(n // i)
    return sum(divisores)

def numeros_amigables(a, b):
    return divisores_propios(a) == b and divisores_propios(b) == a

