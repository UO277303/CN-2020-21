# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:42:02 2021

@author: Héctor
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
import sympy as sym

#%% Definición de funciones

x = sym.Symbol('x',real=True)

f_sim = x**2 + sym.ln(2*x+7)*sym.cos(3*x) + 0.1
df_sim = sym.diff(f_sim,x)
d2f_sim = sym.diff(df_sim,x)

f = sym.lambdify([x],f_sim,'numpy')
df = sym.lambdify([x],df_sim,'numpy')
d2f = sym.lambdify([x],d2f_sim,'numpy')

#%% Extremos

x = np.linspace(-1,3)

plt.figure()
plt.plot(x,df(x))
plt.plot(x,x*0,'k-')
plt.title('Función derivada de f')
plt.show()

x0 = np.array([-1.,0,1.,2.3,2.8])
s = op.newton(df,x0,tol=1.e-6,maxiter=100)
print('EXTREMOS\n',s,'\n\n')

minr = np.array([s[0],s[2],s[4]])
maxr = np.array([s[1],s[3]])

x = np.linspace(-2,4)

plt.figure()
plt.plot(x,f(x),label='Función f')
plt.plot(x,x*0,'k-')
plt.plot(maxr,f(maxr),'ro',label='Extremos superiores')
plt.plot(minr,f(minr),'go',label='Extremos inferiores')
plt.legend()
plt.show()

#%% Puntos de inflexión

x = np.linspace(-1,4)

plt.figure()
plt.plot(x,d2f(x))
plt.plot(x,x*0,'k-')
plt.title('Función derivada segunda de f')
plt.show()

x0 = np.array([-0.4,0.5,1.6,2.5,3.7])
s = op.newton(d2f,x0,tol=1.e-6,maxiter=100)
print('PUNTOS DE INFLEXIÓN EN [-1,4]\n',s)

x = np.linspace(-2,4)

plt.figure()
plt.plot(x,f(x),label='Función f')
plt.plot(x,x*0,'k-')
plt.plot(s,f(s),'bo',label='Puntos de inflexión')
plt.legend()
plt.show()