# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:46:30 2021

@author: Héctor
"""
import numpy as np

#%%

def triangulariza(A,b):
    At = np.copy(A)
    bt = np.copy(b)
    
    m,n = np.shape(A)
    
    for k in range(0,m-1,1):
        f = At[k+1][0]/At[k][1]
        At[k+1][0] = At[k+1][0] - f*At[k][1]
        At[k+1][1] = At[k+1][1] - f*At[k][2]
        bt[k+1] = bt[k+1] - f*bt[k]
    
    return At,bt

def sust_reg(At,bt):
    x = np.copy(bt)
    
    m,n = np.shape(At)
    
    for k in range(m-1,-1,-1):
        if k==m-1:
            x[k] = bt[k]/At[k][1]
        else:
            x[k] = (bt[k]-At[k][2]*x[k+1])/At[k][1]
    
    return x

#%%

n = 7 
Ar = np.zeros((n,3))
Ar[:,0] = np.concatenate((np.array([0]),np.ones((n-1),)))
Ar[:,1] = np.ones((n),)*3
Ar[:,2] = np.concatenate((np.ones((n-1),),np.array([0])))
b = np.arange(n,2*n)*1.

At,bt = triangulariza(Ar,b)

x = sust_reg(At,bt)

print("------------ DATOS ------------")
print("Ar\n",Ar,"\n\nb\n",b,"\n\n")
print("-------- SISTEMA TRIANGULARIZADO --------")
print("At\n",At,"\n\n")
print("-------- SOLUCIÓN ---------")
print("x\n",x,"\n\n\n")


n = 8
np.random.seed(3)
Ar = np.zeros((n,3))
Ar[:,1] = np.random.rand(n)
Ar[:,0] = np.concatenate((np.array([0]),np.random.rand(n-1)))
Ar[0:n-1,2] = Ar[1:n,0]
b = np.random.rand(n)

At,bt = triangulariza(Ar,b)

x = sust_reg(At,bt)

print("------------ DATOS ------------")
print("Ar\n",Ar,"\n\nb\n",b,"\n\n")
print("-------- SISTEMA TRIANGULARIZADO --------")
print("At\n",At,"\n\n")
print("-------- SOLUCIÓN ---------")
print("x\n",x,"\n\n\n")