# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:31:02 2021

@author: Héctor
"""

import numpy as np
import sympy as sym

x = sym.Symbol('x',real=True)
f_sim = sym.log(x)

f = lambda x: np.log(x)
a = 1.
b = 3.

sol = float(sym.integrate(f_sim,(x,a,b)))

#%%
def punto_medio(f,a,b):
    return (b-a)*f((a+b)/2)

sol_aprx = punto_medio(f,a,b)

print('--- Fórmula del punto medio ---')
print('El valor aproximado es ',sol_aprx)
print('El valor exacto es ',sol)

#%%
def trapecio(f,a,b):
    return (b-a)/2*(f(a)+f(b))

sol_aprx = trapecio(f,a,b)

print('\n--- Fórmula del trapecio ---')
print('El valor aproximado es ',sol_aprx)
print('El valor exacto es ',sol)

#%%
def simpson(f,a,b):
    return (b-a)/6*(f(a)+4*f((a+b)/2)+f(b))

sol_aprx = simpson(f,a,b)

print('\n--- Fórmula de Simpson ---')
print('El valor aproximado es ',sol_aprx)
print('El valor exacto es ',sol)
