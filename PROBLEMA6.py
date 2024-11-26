#Sumas parciales de Fibonacci: Implementa un algoritmo para calcular la 
#suma de los primeros N términos de la serie de Fibonacci.

def suma_parcial_fibonacci():
    
    N = int(input("Introduce el número de términos de Fibonacci a sumar: "))
    
    if N <= 0:
        print("El número de términos debe ser positivo.")
        return None
    
    fibonacci = [0, 1]
    
    while len(fibonacci) < N:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    suma = sum(fibonacci[:N])
    
    print(f"La suma de los primeros {N} términos de la serie de Fibonacci es: {suma}")
