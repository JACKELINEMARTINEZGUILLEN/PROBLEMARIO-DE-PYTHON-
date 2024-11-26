#Visualización de raíces: Representa gráficamente un polinomio P(x) y 
#marca en la gráfica las raíces reales calculadas.

def graficar_polinomio_y_raices(coeficientes):
    p = np.poly1d(coeficientes)
    
    raices = [r.real for r in np.roots(coeficientes) if np.isreal(r)]
    
    x_vals = np.linspace(-10, 10, 400)
    y_vals = p(x_vals)


    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='P(x)', color='purple')
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.7)

    for raiz in raices:
        plt.scatter([raiz], [0], color='red', label=f'Raíz: {raiz:.2f}')

    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.title('Gráfica del Polinomio y sus Raíces Reales')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()
  
