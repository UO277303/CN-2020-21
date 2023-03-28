# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 15:07:13 2021

@author: Héctor
"""
import numpy as np

#%%

def busquedaIncremental(f,a,b,n):
    
    intervalos = np.zeros((n,2))
    count = 0
    longitud = (b-a)/n
    x = a
    y = a+longitud
    
    while y <= b:
        if (f(x)*f(y) < 0):
            intervalos[count][0] = x
            intervalos[count][1] = y
            count+=1
        x = x+longitud
        y = y+longitud
        
    intervalos = intervalos[:count,:]
    return intervalos

#%%

f = lambda x: (x**5 - 3*x**2 + 1.6)
a = -1.
b = 1.5
n = 25

m = busquedaIncremental(f,a,b,n)
print("Intervalos que contienen raíces de f1\n\n",m,"\n\n")

f = lambda x: (x + 2)* np.cos(2*x)
a = 0
b = 10
n = 100

m = busquedaIncremental(f,a,b,n)
print("Intervalos que contienen raíces de f2\n\n",m)