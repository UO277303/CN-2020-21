# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:45:54 2021

@author: Héctor
"""
import numpy as np
np.set_printoptions(precision = 8)
np.set_printoptions(suppress = True)

#%%
def jacobi(A,b,tol,maxiter=1000):
    n = len(A)
    x = np.zeros(n)
    
    num_iter = 1
    xant = np.copy(x)
    for i in range(n):
        sum1 = np.sum(A[i, :i] * xant[:i])
        sum2 = np.sum(A[i, i+1:] * xant[i+1:])
        x[i] = 1/A[i][i] * (b[i] -sum1 -sum2)
        
    while np.linalg.norm(x-xant) >= tol and num_iter < maxiter:
        num_iter += 1
        xant = np.copy(x)
        for i in range(n):
            sum1 = np.sum(A[i, :i] * xant[:i])
            sum2 = np.sum(A[i, i+1:] * xant[i+1:])
            x[i] = 1/A[i][i] * (b[i] -sum1 -sum2)
    return x,num_iter

#%%
A = np.array([[5.,1,-1,-1],[1,4,-1,1],[1,1,-5,-1],[1,1,1,-4]])
b = np.array([1.,1,1,1])

x,i = jacobi(A,b,1.e-6)
xs = np.linalg.solve(A,b)

print('------------- Sistema 1 -------------\n\n---- Datos ----\nA')
print(A,'\nb\n',b)
print('\n---- Solución ----\n\n',i,' iteraciones\n')
print('x aproximada\n',x)
print('\nx exacta\n',xs)

n = 9 
A1 = np.diag(np.ones(n))*2 
A2 = np.diag(np.ones(n-1),1)
A = A1 + A2 + A2.T 
b = np.concatenate((np.arange(1.,6),np.arange(4,0,-1)))*1

x,i = jacobi(A,b,1.e-6)
xs = np.linalg.solve(A,b)

print('\n------------- Sistema 2 -------------\n\n---- Datos ----\nA')
print(A,'\nb\n',b)
print('\n---- Solución ----\n\n',i,' iteraciones\n')
print('x aproximada\n',x)
print('\nx exacta\n',xs)
