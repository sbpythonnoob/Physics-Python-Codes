#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 22:36:48 2024

@author: alzaffer
"""

import numpy as np
import matplotlib.pyplot as plt


#Define The Logistic Map
def lmp(x,r):
    return x * r * (1-x)

r = float(input("give me The Growth Rate: "))
x = np.linspace(0,1,1000)

plt.plot(x, lmp(x,r), color = 'black', label = 'function')
plt.plot(x,x, label = 'slope')

#Plot the Cobweb Diagram
x0 = float(input("Give me The Initial Value: "))


for _ in range(100):
    y = lmp(x0,r)
    plt.plot([x0,x0], [x0,y], 'k--', color = 'red', linewidth = '0.5')
    plt.plot([x0,y], [y,y], 'k--', color = 'red', linewidth = '0.5')
    x0 = y
    

plt.title("Cobweb Diagram")
plt.xlabel('Xn')
plt.ylabel('X(n+1)')
plt.axis('equal')
plt.legend()
plt.grid()
