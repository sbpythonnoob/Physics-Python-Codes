#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:51:02 2024

@author: alzaffer
"""

import numpy as np
import matplotlib.pyplot as plt

steps = int(input("Number of steps want to perform: "))
n = np.zeros(steps + 1)
x = np.zeros(steps + 1)
n[0]= float(input("Give me time stamps: "))
x[0] = float(input("Give me intial Value: "))
a = float(input("Give me Growth rate: "))

for i in range(steps):
    x[i+1] = a * x[i] * (1 - x[i])
    n[i+1] = n[i]+1

fig, ax = plt.subplots()
ax.plot(n, x, alpha=0.5)
ax.set(xlabel='n', ylabel='Xn')
plt.grid()
plt.show()
