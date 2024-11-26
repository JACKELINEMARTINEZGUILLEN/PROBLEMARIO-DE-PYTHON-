#Derivadas simbólicas: Diseña una función que acepte una expresión 
#algebraica (por ejemplo, 3x^2 + 2x) y calcule su derivada simbólica.

import sympy as sp

def derivada_simbolica(expr):

x = sp.symbols('x')

expr_sym = sp.sympify(expr)

derivada = sp.diff(expr_sym, x)
    return derivada
