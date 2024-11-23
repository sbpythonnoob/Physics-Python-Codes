#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:22:27 2024

@author: alzaffer
"""

import numpy as np
import matplotlib.pyplot as plt

# Function for the logistic map
def logistic_map(x, r):
    return r * x * (1 - x)

# Generate x values for plotting the function
x = np.linspace(0, 1, 1000)

# Define the growth rate
r = 2.50

# Plot the function and the line y = x
plt.plot(x, logistic_map(x, r), label=f"f(x) = {r}x(1-x)")
plt.plot(x, x, 'k--', label="y = x")

# Initial condition
x0 = 0.2

# Plot the cobweb diagram
xn = x0
for _ in range(100):
    yn = logistic_map(xn, r)
    plt.plot([xn, xn], [xn, yn],'k--', color = 'red', linewidth = '0.5') 
    plt.plot([xn, yn], [yn, yn], 'k--', color = 'black',linewidth = '0.5')
    xn = yn



# Set labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f"Cobweb Diagram for r = {r}, x0 = {x0}")
plt.legend()
plt.axis('equal')  # Ensure aspect ratio is equal
plt.show()
