#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:32:14 2024

@author: alzaffer
"""

import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x0, iterations):
    x = np.zeros(iterations)
    x[0] = x0
    for i in range(1, iterations):
        x[i] = r * x[i - 1] * (1 - x[i - 1])
    return x

# Parameters
growth_rates = [2.5, 3.0, 3.5, 3.9]
x0 = 0.5
iterations = 100

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

for ax, r in zip(axs.flatten(), growth_rates):
    x = logistic_map(r, x0, iterations)
    ax.plot(x, label=f'Growth Rate: {r}')
    ax.set_title(f'Logistic Map for r={r}')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Population')
    ax.legend()

plt.tight_layout()
plt.show()
