# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:17:33 2021

@author: Héctor
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

#%%
a = 1.
b = 2.
h = 0.1

x = np.linspace(a,b,11)
xp = x[:len(x)-1]
xr = x[1:]
xc = x[1:len(x)-1]

f = lambda x: np.log(x)
df = lambda x: 1/x

df_p = (f(xp+h) - f(xp))/h
df_r = (f(xr) - f(xr-h))/h
df_c = (f(xc+h) - f(xc-h))/(2*h)

plt.figure()
plt.title('Derivada de f(x) = ln(x) y sus aproximaciones (h=0.1)')
plt.plot(x,df(x),'--',label='df')
plt.plot(xp,df_p,label='df_p')
plt.plot(xr,df_r,'g',label='df_r')
plt.plot(xc,df_c,'r',label='df_c')
plt.grid()
plt.legend()
plt.show()

ep = np.abs(df(xp) - df_p)
er = np.abs(df(xr) - df_r)
ec = np.abs(df(xc) - df_c)

plt.figure()
plt.title('Errores (h=0.1)')
plt.plot(xp,ep,'o',label='df_p')
plt.plot(xr,er,'o',label='df_r')
plt.plot(xc,ec,'go',label='df_c')
plt.grid()
plt.legend()
plt.show()

print('h = ',h)
egp = norm(ep) / norm(np.abs(df(xp)))
print('ErrorG_p = ',egp)
egr = norm(er) / norm(np.abs(df(xr)))
print('ErrorG_r = ',egr)
egc = norm(ec) / norm(np.abs(df(xc)))
print('ErrorG_c = ',egc)

#%%
h = 0.01

x = np.linspace(a,b,101)
xp = x[:len(x)-1]
xr = x[1:]
xc = x[1:len(x)-1]

df_p = (f(xp+h) - f(xp))/h
df_r = (f(xr) - f(xr-h))/h
df_c = (f(xc+h) - f(xc-h))/(2*h)

plt.figure()
plt.title('Derivada de f(x) = ln(x) y sus aproximaciones (h=0.01)')
plt.plot(x,df(x),'--',label='df')
plt.plot(xp,df_p,label='df_p')
plt.plot(xr,df_r,'g',label='df_r')
plt.plot(xc,df_c,'r',label='df_c')
plt.grid()
plt.legend()
plt.show()

ep = np.abs(df(xp) - df_p)
er = np.abs(df(xr) - df_r)
ec = np.abs(df(xc) - df_c)

plt.figure()
plt.title('Errores (h=0.01)')
plt.plot(xp,ep,'o',label='df_p')
plt.plot(xr,er,'o',label='df_r')
plt.plot(xc,ec,'go',label='df_c')
plt.grid()
plt.legend()
plt.show()

print('h = ',h)
egp = norm(ep) / norm(np.abs(df(xp)))
print('ErrorG_p = ',egp)
egr = norm(er) / norm(np.abs(df(xr)))
print('ErrorG_r = ',egr)
egc = norm(ec) / norm(np.abs(df(xc)))
print('ErrorG_c = ',egc)
