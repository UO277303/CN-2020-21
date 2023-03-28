# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:13:40 2021

@author: Héctor
"""

import numpy as np

#%% 

x0 = -0.4
tol = 1.e-8

factorial = 1.
polinomio = 0.

error = np.inf
i = 0
maxNumSum = 100

while error > tol and i < maxNumSum:
    
    sumando = x0**i / factorial
    polinomio += sumando
    
    error = np.abs(sumando)
    factorial *= i+1
    
    i+=1


print('Valor de la función en -0.4      = ',np.exp(x0))
print('Valor de la aproximación en -0.4 = ',polinomio)
print('Número de iteraciones            = ',i)

