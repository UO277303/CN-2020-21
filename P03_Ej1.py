# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:24:37 2021

@author: Héctor
"""
import numpy as np

#%%

def triangulariza(A,b):
    At = np.copy(A)
    bt = np.copy(b)
    
    m,n = np.shape(A)
    
    for k in range(0,m-1,1):
        f = At[k+1][k]/At[k][k]
        At[k+1][k] = At[k+1][k] - f*At[k][k]
        At[k+1][k+1] = At[k+1][k+1] - f*At[k][k+1]
        bt[k+1] = bt[k+1] - f*bt[k]
    
    return At,bt
    
#%%

np.set_printoptions(precision = 2)
np.set_printoptions(suppress = True)

n = 7
A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),1)
A = A1 + A2 + A2.T
b = np.arange(n,2*n)*1.

At,bt = triangulariza(A,b)

print("------------ DATOS ------------")
print("A\n",A,"\n\nb\n",b,"\n")
print("-------- SISTEMA TRIANGULARIZADO --------")
print("At\n",At,"\n\nbt\n",bt,"\n\n")

n = 8
np.random.seed(3)
A1 = np.diag(np.random.rand(n))
A2 = np.diag(np.random.rand(n-1),1)
A = A1 + A2 + A2.T
b = np.random.rand(n)

At,bt = triangulariza(A,b)

print("------------ DATOS ------------")
print("A\n",A,"\n\nb\n",b,"\n")
print("-------- SISTEMA TRIANGULARIZADO --------")
print("At\n",At,"\n\nbt\n",bt,"\n\n")

