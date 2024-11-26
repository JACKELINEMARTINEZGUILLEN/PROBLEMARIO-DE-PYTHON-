#Factorial: Pedir por teclado N y calcular el Factorial de N:  
#(N! = 1 * 2 * 3 * ... * N)

def calcular_factorial():
   
    N = int(input("Introduce un número entero para calcular su factorial: "))
    
  
    if N < 0:
        print("El factorial no está definido para números negativos.")
        return None
    
    
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i

    print(f"El factorial de {N} es: {factorial}")
