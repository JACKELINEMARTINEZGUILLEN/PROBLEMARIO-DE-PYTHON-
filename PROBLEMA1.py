#Fibonacci inverso: Implementa una función que calcule los primeros N 
#números de la serie de Fibonacci en orden inverso.
def fibonacci_inverso(N):
    
    fib = [0, 1]
    for _ in range(2, N):
        fib.append(fib[-1] + fib[-2])
  
    return fib[::-1]
