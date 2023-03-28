# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:22:35 2021

@author: Héctor
"""

import numpy as np
import matplotlib.pyplot as plt

def funExp(x, tol, maxNumSum):  
    i = 0
    error = np.inf
    factorial = 1.
    polinomio = 0.
    
    y = np.zeros_like(x)
    
    while error > tol and i < maxNumSum:
        
        sumando = x**i / factorial
        polinomio += sumando
        
        error = np.max(abs(sumando))
        factorial *= i+1
        
        y = polinomio
        
        i+=1
        
    return y

f = lambda x: np.exp(x)

#%%
x = np.linspace(-1,1,50)
tol = 1.e-8
maxNumSum = 100

s = funExp(x,tol,maxNumSum)

plt.plot(x,f(x),'y',linewidth=5,label='f')
plt.plot(x,s,'b--',label='Aproximacion f')
plt.plot(x,x*0,'k')
plt.legend()
plt.grid()
plt.title('Aproximacion de f con el polinomio de McLaurin')

