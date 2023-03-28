# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:19:37 2021

@author: Héctor
"""
import numpy as np
import matplotlib.pyplot as plt

#%%

def lagrange_fund(k,x,z):
    
    lt = np.zeros_like(z)
    
    for n in range(len(z)):
    
        i = 0
        l = 1
        
        while i<k:
            aux = z[n] - x[i]
            aux /= (x[k] - x[i])
            l *= aux
            i+=1
        
        i = len(x) -1
        while i>k:
            aux = z[n] - x[i]
            aux /= (x[k] - x[i])
            l *= aux
            i-=1
        
        lt[n] = l
    
    return lt

def polinomio_lagrange(x,y,z):
    
    p = np.zeros_like(z)
    i = 0
    
    while i<len(x):
        p += lagrange_fund(i,x,z) * y[i]
        i+=1
    
    return p

#%%

x = np.array([-1.,0,2,3,5])
xp = np.linspace(min(x),max(x))
y = np.array([1.,3,4,3,1])

z = xp
p = polinomio_lagrange(x,y,z)

plt.figure()
plt.plot(xp,p,label = 'p')
plt.plot(x,y,'ro',label = 'puntos')
plt.legend()
plt.grid()
plt.show()

x = np.array([-1.,0,2,3,5,6,7])
xp = np.linspace(min(x),max(x))
y = np.array([1.,3,4,3,2,2,1])

z = xp
p = polinomio_lagrange(x,y,z)

plt.figure()
plt.plot(xp,p,label = 'p')
plt.plot(x,y,'ro',label = 'puntos')
plt.legend()
plt.grid()
plt.show()
