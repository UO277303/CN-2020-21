# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:12:43 2021

@author: Héctor
"""

import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision = 2)
np.set_printoptions(suppress = True)

#%%
def aprox1(f,g,a,b,n):
    x = np.linspace(a,b,n)
    y = f(x)
    
    V = np.ones((len(x),g+1))
    
    for j in range(1,g+1):
        for i in range(n):
                V[i][j] = x[i]**j
    
    C = np.dot(np.transpose(V),V)
    d = np.dot(np.transpose(V),y)
    
    p = np.linalg.solve(C,d)
    p = p[::-1]
    
    xaux = np.linspace(a,b,50)
    yaux = np.polyval(p,xaux)
    
    plt.figure()
    plt.plot(xaux,yaux,label='función aproximada')
    plt.plot(x,y,'ro',label='puntos')
    plt.legend()
    plt.show()              

#%%
f = lambda x: np.sin(x)
a = 0
b = 2
n = 5
g = 2
aprox1(f,g,a,b,n)

f = lambda x: np.cos(np.arctan(x))-np.log(x+5)
a = -2
b = 0
n = 10
g = 4
aprox1(f,g,a,b,n)