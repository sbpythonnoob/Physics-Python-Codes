#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 08:01:33 2024

@author: alzaffer
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate x values for plotting the function
x = np.linspace(0,1)

# Define the growth rate
r = 3.99
# Function for the logistic map
def logistic_map(x, r):
    return r * x * (1 - x)

# Plot the function and the line y = x
plt.plot(x, logistic_map(x,r), label = 'Function')
plt.plot(x,x,'k--', color = 'red', label = 'y = x')
plt.title('Xn vs X(n+1)')
plt.xlabel('Xn')
plt.ylabel('X(n+1)')
plt.axis('equal')
plt.legend()
plt.grid()



