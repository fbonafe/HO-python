#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:25:04 2017

@author: franco
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x,a,b):
    return a*x + b

data = np.genfromtxt('tabla.dat')
x = data[:,0]
y = data[:,1]
xfit = np.linspace(x.min()-0.5, x.max()+0.5, 1000)
popt, pcov = curve_fit(func, x, y)
yfit = func(xfit, popt[0], popt[1])

plt.scatter(x,y)
plt.plot(xfit, yfit, color='red')
plt.xlim(x.min()-0.5, x.max()+0.5)
plt.ylim(y.min()-0.5, y.max()+0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('ex2.png', bbox_inches=0, dpi=600)



