# -*- coding: utf-8 -*-
"""
Created on Sat May  1 15:54:55 2021

@author: Héctor
"""
import numpy as np
np.set_printoptions(precision = 2)
np.set_printoptions(suppress = True)

#%%
def sust_regre(U, b):
    n = len(U)
    sol = np.zeros_like(b)
    for i in range(n-1,-1,-1):
        res = 0
        for j in range(i+1,n,1):
            res += U[i][j]*sol[j]
        sol[i] = (1/U[i][i])*(b[i]-res)
    return sol

#%%
U = np.array([[2., 1, 1], [0, 2, 1], [0, 0, 2]])
b = np.array([9., 4, 4])

x = sust_regre(U, b)

print('------------- SISTEMA 1 -------------')
print('\n--- Datos ---\nU\n',U,'\nb\n',b)
print('\n--- Solución ---\nx\n',x)

n = 5
np.random.seed(2)           
U = np.random.random((n,n)) 
U = np.triu(U)
b = np.random.random(n)

x = sust_regre(U, b)

print('\n\n------------- SISTEMA 2 -------------')
print('\n--- Datos ---\nU\n',U,'\nb\n',b)
print('\n--- Solución ---\nx\n',x)