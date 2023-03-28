# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 20:54:31 2021

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


def divisores(m):
    
    div = np.zeros(int(m*2))
    
    count = 0
    num = 1
    n = 0
    
    while num <= m:
        if np.remainder(m,num) == 0:
            div[count] = num
            div[count+1] = num*-1
            n+=2
            count+=2
        num+=1
    
    div = div[:n]
    return div


def raices(p):
    
    result = np.zeros(len(p)-1)
    count = 0
    d = divisores(np.abs(p[-1]))
    
    while count < len(result):
        i = 0
        while i < len(d):
            c,r = horner(p,d[i])
            if r== 0:
                raiz = d[i]
                p = c
                break
            i+=1
        result[count] = raiz
        count+=1
        
    return result
    
    
    

#%%

print("\n(a)\n")
print("Divisores de 6")
print(divisores(6),"\n")
print("Divisores de 18")
print(divisores(18),"\n")
print("Divisores de 20")
print(divisores(20),"\n\n")

#%%

p0 = np.array([1.,0,-1])
p1 = np.array([1.,-3,-6,8])
p2 = np.array([1.,2,-16,-2,15])
p3 = np.array([1.,-5,-13,53,60])
p4 = np.array([1.,4,-56,-206,343,490])

print("(b)\n")
print("Raíces de p0")
print(raices(p0),"\n")
print("Raíces de p1")
print(raices(p1),"\n")
print("Raíces de p2")
print(raices(p2),"\n")
print("Raíces de p3")
print(raices(p3),"\n")
print("Raíces de p4")
print(raices(p4),"\n")