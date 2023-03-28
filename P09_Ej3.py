# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:31:03 2021

@author: Héctor
"""

import numpy as np
import sympy as sym
from scipy.integrate import fixed_quad

a = 1.
b = 3.

#%%
def punto_medio(f,a,b):
    return (b-a)*f((a+b)/2),0

def trapecio(f,a,b):
    return (b-a)/2*(f(a)+f(b)),0

def simpson(f,a,b):
    return (b-a)/6*(f(a)+4*f((a+b)/2)+f(b)),0

def grado_de_precision(formula):
    g = 0
    e = 0.
    for i in range(100):
        f = lambda x: x**i
        x = sym.Symbol('x',real=True)
        f_sim = x**i
        sol = float(sym.integrate(f_sim,(x,a,b)))
        e = np.abs(sol - formula(f,a,b)[0])
        g = i-1
        print('f(x) = x^',i,'\t error = ',e)
        if (e > 10**-11):
            e = 0.0
            break
    print('\nEl grado de precisión es ',g,'\n')

#%%
print('--- Fórmula del punto medio ---')
grado_de_precision(punto_medio)

print('--- Fórmula del trapecio ---')
grado_de_precision(trapecio)

print('--- Fórmula de Simpson ---')
grado_de_precision(simpson)

print('--- Fórmula fixed_squad ---')
grado_de_precision(fixed_quad)
