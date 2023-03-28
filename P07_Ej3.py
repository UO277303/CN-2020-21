# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:35:18 2021

@author: Héctor
"""
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision = 2)
np.set_printoptions(suppress = True)

#%%
def aprox2(f,g,a,b):
    x = np.linspace(a,b)
    y = f(x)
    
    V = np.ones((len(x),g+1))
    
    for j in range(1,g+1):
        for i in range(len(x)):
                V[i][j] = x[i]**j
    
    C = np.dot(np.transpose(V),V)
    d = np.dot(np.transpose(V),y)
    p = np.linalg.solve(C,d)
    p = p[::-1]
    
    x = np.linspace(a,b,50)
    y = np.polyval(p,x)
    
    plt.figure()
    plt.plot(x,y,label='función aproximada')
    plt.plot(x,f(x),'r',label='función exacta')
    plt.legend()
    plt.show()

#%%
f = lambda x: np.sin(x)
a = 0
b = 2
g = 2
aprox2(f,g,a,b)

f = lambda x: np.cos(np.arctan(x))-np.log(x+5)
a = -2
b = 0
g = 4
aprox2(f,g,a,b)