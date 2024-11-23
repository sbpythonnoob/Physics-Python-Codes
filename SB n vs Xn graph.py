#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 08:06:33 2024

@author: alzaffer
"""

import numpy as np
import matplotlib.pyplot as plt

ni = 50 #number of steps
n = np.zeros(ni +1)
Xn = np.zeros(ni +1 )

n[0] = 0
Xn[0] = 0.10
r = 2.99 #Growth Rate #for 2 period r = 3.3
Xni = []

for i in range(ni):
    Xn[i +1] = r * Xn[i] * (1 - Xn[i])
    n[i+1] = n[i] + 1
    
    

#ax = plt.axes(projection = '3d')    
plt.plot(n, Xn, 'k--', color = 'brown', label = 'function')
plt.xlabel('n')
plt.ylabel('Xn')
plt.title('n vs Xn graph 4 period')
plt.legend()
plt.grid()
