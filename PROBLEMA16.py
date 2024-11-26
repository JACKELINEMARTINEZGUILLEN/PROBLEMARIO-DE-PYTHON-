#Raíces de polinomios: Diseña un programa que encuentre todas las raíces 
#reales de un polinomio de tercer grado
from numpy.linalg import LinAlgError

def raices_polinomio(coeficientes):
    if len(coeficientes) != 4:
        raise ValueError("Debe ser un polinomio de tercer grado (4 coeficientes).")
    
    raices = np.roots(coeficientes)
    
    raices_reales = [r.real for r in raices if np.isreal(r)]
    return raices_reales
