#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:25:12 2017

@author: franco
"""

from scipy import misc, interpolate
import matplotlib.pyplot as plt
import numpy as np

def poly(x):
    return x**3+x**2-4*x+4

def derspline(f, xrange):
    yrange = f(xrange)
    spl = interpolate.UnivariateSpline(xrange, yrange, k=4)
    return spl, spl.derivative()
    
    
xmin = -10
xmax = 10
x = np.linspace(xmin, xmax, 1000)
spl, dpoly = derspline(poly, x)
pcriticos = dpoly.roots()
print('El maximo es {}'.format(max(poly(pcriticos))))


#dpoly = misc.derivative(poly, x, dx=1.0e-6, n=1)
#plt.plot(x, spl(x), 'r--')
plt.plot(x, poly(x), label='funcion')
plt.plot(x, dpoly(x), label='derivada')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.savefig('ex3.png', dpi=600)

dx = 0.1
xdump = np.linspace(xmin, xmax, int((xmax-xmin)/0.1))
vecdump = np.c_[xdump, poly(xdump)]
np.savetxt('ex3_dump.dat', vecdump)
