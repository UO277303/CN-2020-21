# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 16:30:56 2021

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

def biseccion(f,a,b,tol=1.e-6,maxiter=100):
    
    sol = 0
    it = 0
    x = (a+b)/2
    
    while (it < maxiter and
            np.abs(b-a) >= tol):
        x = (a+b)/2
        if (f(a)*f(x) < 0):
            b = x
            it+=1
        elif (f(x)*f(b) < 0):
            a = x
            it+=1
        else:
            break
    
    sol = x
    
    return sol,it
    
#%%

f = lambda x: (x**5 - 3*x**2 + 1.6)
a = -1.
b = 1.5
n = 25
m = busquedaIncremental(f,a,b,n)

s,i = biseccion(f,m[0][0],m[0][1])
print(s,i)

s,i = biseccion(f,m[1][0],m[1][1])
print(s,i)

s,i = biseccion(f,m[2][0],m[2][1])
print(s,i)
