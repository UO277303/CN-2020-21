# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:28:09 2021

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

def newton(f,df,x0,tol=1.e-6,maxiter=100):
    
    sol = 0
    it = 1
    xa = x0
    x = xa - (f(xa)/df(xa))
    
    while (it < maxiter and
           np.abs(x-xa) >= tol):
        xa = x
        x = xa - (f(xa)/df(xa))
        it+=1
    
    sol = x
    
    return sol,it

#%%

f = lambda x: x**5 - 3*x**2 + 1.6
df = lambda x: 5*x**4 - 6*x

a = -1.
b = 1.5
n = 25
m = busquedaIncremental(f,a,b,n)

s,i = newton(f,df,-0.7)
print(s,i)

s,i = newton(f,df,0.8)
print(s,i)

s,i = newton(f,df,1.2)
print(s,i)