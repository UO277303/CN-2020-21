# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:19:39 2021

@author: Héctor
"""
import numpy as np
import matplotlib.pyplot as plt

#%%

def chebyshev(f,a,b,n):
    x = np.zeros(n)
    i = 1
    aux = 0
    
    while aux<n:
        x[aux] = np.cos(((2*i - 1)*np.pi)/(2*n))
        i+=1
        aux+=1

    return x

#%%
a = -1
b = 1
xp = np.linspace(a,b,300)

f = lambda x: 1/(1 + 25*x**2)
n = 11

c = chebyshev(f,a,b,n)
ne = np.linspace(a,b,n)

pol = np.polyfit(ne,f(ne),len(ne)-1)
yp = np.polyval(pol,xp)

plt.figure()
plt.axis([-1.05,1.05,-0.3,2.3])
plt.plot(xp,f(xp),'b',label='función')
plt.plot(ne,f(ne),'ro',label='nodos')
plt.plot(xp,yp,'r',label='polinomio')
plt.title('Nodos equiespaciados f1')
plt.legend()
plt.show()

pol = np.polyfit(c,f(c),len(c)-1)
yp = np.polyval(pol,xp)

plt.figure()
plt.axis([-1.05,1.05,-0.3,2.3])
plt.plot(xp,f(xp),'b',label='función')
plt.plot(c,f(c),'ro',label='nodos')
plt.plot(xp,yp,'r',label='polinomio')
plt.title('Nodos Chebyshev f1')
plt.legend()
plt.show()

#%%
f = lambda x: np.exp(-20*x**2)
n = 15

c = chebyshev(f,a,b,n)
ne = np.linspace(a,b,n)

pol = np.polyfit(ne,f(ne),len(ne)-1)
yp = np.polyval(pol,xp)

plt.figure()
plt.axis([-1.05,1.05,-0.3,2.3])
plt.plot(xp,f(xp),'b',label='función')
plt.plot(ne,f(ne),'ro',label='nodos')
plt.plot(xp,yp,'r',label='polinomio')
plt.title('Nodos equiespaciados f2')
plt.legend()
plt.show()

pol = np.polyfit(c,f(c),len(c)-1)
yp = np.polyval(pol,xp)

plt.figure()
plt.axis([-1.05,1.05,-0.3,2.3])
plt.plot(xp,f(xp),'b',label='función')
plt.plot(c,f(c),'ro',label='nodos')
plt.plot(xp,yp,'r',label='polinomio')
plt.title('Nodos Chebyshev f2')
plt.legend()
plt.show()
