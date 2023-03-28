# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 15:05:01 2021

@author: Héctor
"""
import numpy as np

#%%

def horner(p, x):
    
    n = len(p)
    q = np.zeros(n) 
    
    count = 1
    
    q[0] = p[0]
    while count <= n-1:
        q[count] = p[count] + q[count-1]*x
        count+=1
    
    cociente = q[:-1]
    resto = q[-1]
    return cociente, resto    
    
#%%

p0 = np.array([1.,2,1])
x0 = 1.

c, r = horner(p0, x0)

print("Coeficientes de Q = ",c)
print("P0(1) = ",r,"\n")

p1 = np.array([1.,-1,2,-3,5,-2])
x1 = 1.

c, r = horner(p1, x1)

print("Coeficientes de Q = ",c)
print("P1(1) = ",r,"\n")

p2 = np.array([1.,-1,-1,1,-1,0,-1,1])
x2 = -1.

c, r = horner(p2, x2)

print("Coeficientes de Q = ",c)
print("P2(-1) = ",r,"\n")