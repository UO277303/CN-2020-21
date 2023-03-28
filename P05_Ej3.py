# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:57:20 2021

@author: Héctor
"""
import numpy as np
import matplotlib.pyplot as plt

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


def puntoFijo(g,x0,tol=1.e-6,maxiter=200):
    
    i = 1
    x = g(x0)
    
    while (i < maxiter and np.abs(x-x0) >= tol):
        x0 = x
        x = g(x0)
        i+=1
        
    pf = x  
    
    return pf,i

#%%

f = lambda x: np.exp(-x) - x
g = lambda x: np.exp(-x)

intervalo = busquedaIncremental(f,0,1,10)
print('Existe una raíz en ',intervalo,'\n')

pf,it = puntoFijo(g,intervalo[0][0])
print(pf,it,'\n\n')

x = np.linspace(0,1)

plt.figure()
plt.plot(x,g(x),'r',label='g')
plt.plot(x,x,'b',label='y = x')
plt.plot(pf,pf,'bo')
plt.legend()
plt.show()

#%%

f1 = lambda x: x - np.cos(x)
g1 = lambda x: np.cos(x)
g2 = lambda x: 2*x - np.cos(x)
g3 = lambda x: x - (x - np.cos(x))/(1 + np.sin(x))
g4 = lambda x: (9*x + np.cos(x))/10

intervalo = busquedaIncremental(f1,0,1,10)
print('Existe una raíz en ',intervalo)

pf,it = puntoFijo(g1,intervalo[0][0])
print('g1',pf,it)
pf,it = puntoFijo(g2,intervalo[0][0])
print('g2',pf,it)
pf,it = puntoFijo(g3,intervalo[0][0])
print('g3',pf,it)
pf,it = puntoFijo(g4,intervalo[0][0])
print('g4',pf,it)

x = np.linspace(0,1)

plt.figure()
plt.plot(x,g1(x),label='g1')
plt.plot(x,g2(x),label='g2')
plt.plot(x,g3(x),label='g3')
plt.plot(x,g4(x),label='g4')
plt.plot(x,x,'b',label='y = x')
plt.plot(pf,pf,'bo')
plt.legend()
plt.show()

