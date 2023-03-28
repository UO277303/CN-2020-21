# -*- coding: utf-8 -*-
"""
Created on Sat May  1 15:54:54 2021

@author: Héctor
"""
import numpy as np
np.set_printoptions(precision = 2)
np.set_printoptions(suppress = True)

#%%
def gaussjordan(A):
    n = len(A)
    I = np.eye(n)
    M = np.concatenate((A,I),axis=1)
    for k in range(n):
        if (M[k][k] != 0):
            M[k] /= M[k][k]
            for i in range(n):
                if (i != k):
                    M[i] -= M[i][k]*M[k]
    Ainv = A
    for i in range(n):
        for j in range(n):
            Ainv[i][j] = M[i][j+n]
    return Ainv

#%%
A = np.array([[2., 1, 1], [1, 2, 1], [1, 1, 2]])

invA = gaussjordan(A)

print('Matriz\n',A,'\n\nMatriz inversa\n',invA)

n = 5
np.random.seed(3)           
A = np.random.random((n,n))

invA = gaussjordan(A)

print('\n\nMatriz\n',A,'\n\nMatriz inversa\n',invA)
