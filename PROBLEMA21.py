#Pendiente y tangente: Grafica una función como y, 
#en el mismo gráfico, muestra la recta tangente en un punto dado.

def graficar_funcion_y_tangente(f, x0):

    def derivada_numerica(f, x, h=1e-5):
        return (f(x + h) - f(x - h)) / (2 * h)
    
    y0 = f(x0)
    pendiente = derivada_numerica(f, x0)
    
    def tangente(x):
        return pendiente * (x - x0) + y0

    x_vals = np.linspace(x0 - 5, x0 + 5, 400)
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, f(x_vals), label='f(x)', color='blue')
    plt.plot(x_vals, tangente(x_vals), label=f'Tangente en x={x0}', color='orange', linestyle='--')
    plt.scatter([x0], [y0], color='red', label=f'Punto de tangencia ({x0}, {y0})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de la Función y su Tangente en un Punto')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
