# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 19:58:30 2021

@author: Héctor
"""
import numpy as np
import matplotlib.pyplot as plt

#%%

def hornerV(p, x):
    
    n = len(x)
    y = np.zeros(n)
    
    count = 0
    while count <= n-1:
        q = np.zeros(len(p)) 
        
        i = 1
        q[0] = p[0]
        
        while i <= len(p)-1:
            q[i] = p[i] + q[i-1]*x[count]
            i+=1
        
        resto = q[-1]
        y[count] = resto
        count+=1
    
    return y    
    
#%%

x = np.linspace(-1,1)

p = np.array([1.,-1.,2,-3,5,-2])
y = hornerV(p,x)

plt.figure()
plt.plot(x,x*0,'k')
plt.plot(x,y)
plt.title("P")

r = np.array([1.,-1,-1,1,-1,0,-1,1])
y = hornerV(r,x)

plt.figure()
plt.plot(x,x*0,'k')
plt.plot(x,y)
plt.title("R")