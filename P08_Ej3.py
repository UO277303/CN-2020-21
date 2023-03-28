# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:17:35 2021

@author: Héctor
"""
import numpy as np
from numpy.linalg import norm

#%%
f = lambda x: np.cos(2*np.pi*x)
df2 = lambda x: -4*np.pi**2*np.cos(2*np.pi*x)

a = -1.
b = 0.
h = 0.001

x = np.linspace(a,b,int((b-a)/h))

df2_a = (f(x-h) - 2*f(x) + f(x+h))/h**2

ea = np.abs(df2(x) - df2_a)
eg = norm(ea) / norm(np.abs(df2(x)))
print('Error relativo = ',eg)
