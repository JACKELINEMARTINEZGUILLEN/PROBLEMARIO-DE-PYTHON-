#Simulación de ondas: Dibuja la superposición de dos ondas

def simulacion_de_ondas(amplitud1, frecuencia1, fase1, amplitud2, frecuencia2, fase2, duracion=2, tasa_muestreo=1000):
    
    t = np.linspace(0, duracion, int(tasa_muestreo * duracion))
    
    onda1 = amplitud1 * np.sin(2 * np.pi * frecuencia1 * t + fase1)
    onda2 = amplitud2 * np.sin(2 * np.pi * frecuencia2 * t + fase2)
    
    superposicion = onda1 + onda2

    plt.figure(figsize=(12, 8))
    
    plt.subplot(3, 1, 1)
    plt.plot(t, onda1, label='Onda 1', color='blue')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Onda 1')
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.subplot(3, 1, 2)
    plt.plot(t, onda2, label='Onda 2', color='green')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Onda 2')
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.subplot(3, 1, 3)
    plt.plot(t, superposicion, label='Superposición de Ondas', color='purple')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Superposición de las Ondas')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()
