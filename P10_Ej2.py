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

def triang(A, b):
    n = len(A)
    U = A
    for k in range(n):
        if (A[k][k] != 0):
            for i in range(k+1,n,1):
                f = A[i][k]/A[k][k]
                b[i] -= f*b[k]
                U[i] = A[i] - f*A[k]
        k+=1
    return U,b

#%%
A = np.array([[2., 1, 1], [1, 2, 1], [1, 1, 2]])
b = np.array([2., 4, 6])

print('------------- SISTEMA 1 -------------')
print('\n\t\t--DATOS--\nA\n',A,'\nb\n',b)

U,c = triang(A,b)
x = sust_regre(U,c)

print('\n\t\t--TRIANGULARIZACIÓN--\n\nU\n',U)
print('\nc\n',c)
print('\n\t\t--SUSTITUCIÓN REGRESIVA--\nx\n',x)

n = 5
np.random.seed(3)
A = np.random.random((n,n))
b = np.random.random(n)

print('\n------------- SISTEMA 2 -------------')
print('\n\t\t--DATOS--\nA\n',A,'\nb\n',b)

U,c = triang(A,b)
x = sust_regre(U,c)

print('\n\t\t--TRIANGULARIZACIÓN--\n\nU\n',U)
print('\nc\n',c)
print('\n\t\t--SUSTITUCIÓN REGRESIVA--\nx\n',x)
