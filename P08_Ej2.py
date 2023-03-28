# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:17:35 2021

@author: Héctor
"""
import numpy as np
from numpy.linalg import norm

#%%
f = lambda x: x**3 + x**2 + x
a = 0.
b = 1.
h = 0.02

df = lambda x: 3*x**2 + 2*x + 1

x = np.linspace(a,b,int((b-a)/h)+1)

df_p = (f(x+h) - f(x))/h
df_r = (f(x) - f(x-h))/h
df_c = (f(x+h) - f(x-h))/(2*h)

df_o1 = np.zeros(len(x))

df_o1[0] = df_p[0]
df_o1[1:len(df_o1)-1] = df_c[1:len(df_o1)-1]
df_o1[-1] = df_r[-1]

e = np.abs(df(x) - df_o1)
eg = norm(e) / norm(np.abs(df(x)))
print('Error con derivación de orden 1 = ',eg)

#%%
df_p = 1/(2*h)*(-3*f(x) + 4*f(x+h) - f(x+2*h))
df_c = 1/(2*h)*(f(x+h) - f(x-h))  
df_r = 1/(2*h)*(f(x-2*h) - 4*f(x-h) + 3*f(x))

df_o2 = df_c

df_o2[0] = df_p[0]
df_o2[1:len(df_o2)-1] = df_c[1:len(df_o2)-1]
df_o2[-1] = df_r[-1]

e = np.abs(df(x) - df_o2)
eg = norm(e) / norm(df(x))
print('Error con derivación de orden 2 = ',eg)
