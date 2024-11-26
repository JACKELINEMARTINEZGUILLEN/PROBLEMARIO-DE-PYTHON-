#Fibonacci generalizado: Crea una función que reciba dos números 
#iniciales y calcule una serie similar a Fibonacci, pero con estos números 
#como punto de partida.

def fibonacci_generalizado(a, b, N):
   
    fib_gen = [a, b]
    for _ in range(2, N):
        fib_gen.append(fib_gen[-1] + fib_gen[-2])
    return fib_gen
