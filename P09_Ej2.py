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
def punto_medio_comp(f,a,b,n):
    sol = 0.
    h = (b-a)/n
    for i in range(1,n+1):
        x = a + i*h
        xa = a + (i-1)*h
        sol += f((xa+x)/2)
    sol *= h
    return sol

sol_aprx = punto_medio_comp(f,a,b,5)

print('--- Fórmula del punto medio ---')
print('El valor aproximado es ',sol_aprx)
print('El valor exacto es ',sol)

#%%
def trapecio_comp(f,a,b,n):
    sol = 0.
    h = (b-a)/n
    for i in range(1,n):
        x = a + i*h
        sol += f(x)
    sol *= h
    sol += h/2*(f(a)+f(b))
    return sol

sol_aprx = trapecio_comp(f,a,b,4)

print('\n--- Fórmula del punto medio ---')
print('El valor aproximado es ',sol_aprx)
print('El valor exacto es ',sol)

#%%
def simpson_comp(f,a,b,n):
    sol = 0.
    h = (b-a)/n
    for i in range(1,n+1):
        x = a + i*h
        xa = a + (i-1)*h
        sol += f(xa)+4*f((xa+x)/2)+f(x)
    sol *= h/6
    return sol

sol_aprx = simpson_comp(f,a,b,4)

print('\n--- Fórmula del punto medio ---')
print('El valor aproximado es ',sol_aprx)
print('El valor exacto es ',sol)
