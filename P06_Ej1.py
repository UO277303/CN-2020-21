# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:19:35 2021

@author: Héctor
"""
import numpy as np
import matplotlib.pyplot as plt

#%%

def lagrange_fund(k,x,z):
    
    lt = np.zeros_like(z)
    
    for n in range(len(z)):
    
        i = 0
        l = 1
        
        while i<k:
            aux = z[n] - x[i]
            aux /= (x[k] - x[i])
            l *= aux
            i+=1
        
        i = len(x) -1
        while i>k:
            aux = z[n] - x[i]
            aux /= (x[k] - x[i])
            l *= aux
            i-=1
        
        lt[n] = l
    
    return lt

#%%
x = np.array([-1.,0,2,3,5])
xp = np.linspace(min(x),max(x))

z = xp

k = 0
yz = lagrange_fund(k,x,z)
ident = np.eye(len(x))

plt.figure()
plt.plot(xp,xp*0,'k')
plt.plot(xp,yz)
plt.plot(x,ident[k],'o')
plt.title('L0')
plt.grid()
plt.show()

k = 1
yz = lagrange_fund(k,x,z)
ident = np.eye(len(x))

plt.figure()
plt.plot(xp,xp*0,'k')
plt.plot(xp,yz)
plt.plot(x,ident[k],'o')
plt.title('L1')
plt.grid()
plt.show()

k = 2
yz = lagrange_fund(k,x,z)
ident = np.eye(len(x))

plt.figure()
plt.plot(xp,xp*0,'k')
plt.plot(xp,yz)
plt.plot(x,ident[k],'o')
plt.title('L2')
plt.grid()
plt.show()

k = 3
yz = lagrange_fund(k,x,z)
ident = np.eye(len(x))

plt.figure()
plt.plot(xp,xp*0,'k')
plt.plot(xp,yz)
plt.plot(x,ident[k],'o')
plt.title('L3')
plt.grid()
plt.show()

k = 4
yz = lagrange_fund(k,x,z)
ident = np.eye(len(x))

plt.figure()
plt.plot(xp,xp*0,'k')
plt.plot(xp,yz)
plt.plot(x,ident[k],'o')
plt.title('L4')
plt.grid()
plt.show()