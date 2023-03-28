# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:26:03 2021

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

def sust_reg(At,bt):
    x = np.copy(bt)
    
    m,n = np.shape(At)
    
    for k in range(m-1,-1,-1):
        if k==m-1:
            x[k] = bt[k]/At[k][k]
        else:
            x[k] = (bt[k]-At[k][k+1]*x[k+1])/At[k][k]
    
    return x

#%%

np.set_printoptions(precision = 2)
np.set_printoptions(suppress = True)

n = 7
A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),1)
A = A1 + A2 + A2.T
b = np.arange(n,2*n)*1.

At,bt = triangulariza(A,b)

x = sust_reg(At,bt)

print("x\n",x,"\n\n")

n = 8
np.random.seed(3)
A1 = np.diag(np.random.rand(n))
A2 = np.diag(np.random.rand(n-1),1)
A = A1 + A2 + A2.T
b = np.random.rand(n)

At,bt = triangulariza(A,b)

x = sust_reg(At,bt)

print("x\n",x,"\n\n")