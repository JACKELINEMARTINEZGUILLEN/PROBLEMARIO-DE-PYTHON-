#EJERCICIOS DE GRAFICA
#Gráfica de Fibonacci acumulativo: Genera una gráfica de barras donde el 
#eje X representa los índices de la serie de Fibonacci y el eje Y la suma 
#acumulada de los términos hasta ese índice.
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
def fibonacci_acumulativo(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

     suma_acumulada = np.cumsum(fibonacci)

     plt.figure(figsize=(10, 6))
     plt.bar(range(n), suma_acumulada, color='lightblue')
     plt.xlabel('Índice en la serie de Fibonacci')
     plt.ylabel('Suma acumulada')
     plt.title('Suma Acumulada de los Términos de la Serie de Fibonacci')
     plt.grid(axis='y', linestyle='--', alpha=0.7)
     plt.show()
