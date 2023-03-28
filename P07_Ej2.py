# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:59:51 2021

@author: Héctor
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%
df = pd.read_csv('cars.csv',sep=',')

hp = df['horsepower']
w = df['weight']

p = np.polyfit(w,hp,1)
pe = np.polyval(p,3000)

x = np.linspace(1500,5000,392)
px = np.polyval(p,x)

plt.figure()
plt.plot(w,hp,'o')
plt.plot(3000,pe,'ro')
plt.plot(x,px,'r-')
plt.xlabel('weight')
plt.ylabel('horsepower')
plt.show()

mpg = df['mpg']

p = np.polyfit(hp,mpg,2)
mpge = np.polyval(p,pe)

x = np.linspace(50,225,392)
px = np.polyval(p,x)

plt.figure()
plt.plot(hp,mpg,'o')
plt.plot(pe,mpge,'ro')
plt.plot(x,px,'r-')
plt.xlabel('horsepower')
plt.ylabel('mpg')
plt.show()