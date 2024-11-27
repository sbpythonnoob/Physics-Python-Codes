#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:54:11 2024

@author: alzaffer
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the Logistic Map
def lmp(x, r):
    return x * r * (1 - x)

# Define the growth rates
rs = [2.9, 3.1, 3.5, 4.0]

# Define the initial values
x0s = [0.1, 0.1, 0.1, 0.1]

# Create a figure with 4 subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

for i, (r, x0, ax) in enumerate(zip(rs, x0s, axs.flat)):
    x = np.linspace(0, 1, 1000)
    ax.plot(x, lmp(x, r), color='black', label='function')
    ax.plot(x, x, label='slope')

    # Plot the Cobweb Diagram
    for _ in range(100):
        y = lmp(x0, r)
        ax.plot([x0, x0], [x0, y], 'k--', color='red', linewidth=0.5)
        ax.plot([x0, y], [y, y], 'k--', color='red', linewidth=0.5)
        x0 = y

    ax.set_title(f"Cobweb Diagram, r={r}")
    ax.set_xlabel('Xn')
    ax.set_ylabel('X(n+1)')
    ax.axis('equal')
    ax.legend()
    ax.grid()

# Layout so plots do not overlap
fig.tight_layout()

plt.show()
