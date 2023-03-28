# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:33:32 2021

@author: Héctor
"""
import numpy as np
import matplotlib.pyplot as plt

#%%

def secante(f,x0,x1,tol=1.e-6,maxiter=100):
    
    i = 0
    
    xb = x1
    xc = x0
    xa = xb - f(xb)*((xb-xc)/(f(xb)-f(xc)))
    
    while (i < maxiter and np.abs(xb-xc) >= tol):
        
        xa = xb - f(xb)*((xb-xc)/(f(xb)-f(xc)))
        xc = xb
        xb = xa
        
        i+=1
    
    sol = xa
            
    return sol,i

#%%

f = lambda x: x**5 - 3*x**2 + 1.6
r = np.zeros(3)

s,i = secante(f,-0.7,-0.6)
print(s,i)
r[0] = s

s,i = secante(f,0.8,0.9)
print(s,i)
r[1] = s

s,i = secante(f,1.2,1.3)
print(s,i)
r[2] = s


x = np.linspace(-1,1.5)

plt.figure()
plt.plot(x,f(x))
plt.plot(x,x*0,'k')
plt.plot(r,r*0,'ro')
plt.show()
