#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 22:26:23 2024

@author: alzaffer
"""

import numpy as np
import matplotlib.pyplot as plt

# Function for the logistic map
def logistic_map(x, r):
    return r * x * (1 - x)

# Parameters
r_min, r_max = 2.8, 4.0
accuracy = 0.0001
reps = 600  # Number of repetitions to discard transients
num_to_plot = 20  # Number of points to plot after transients

# Generate r values
r_values = np.arange(r_min, r_max, accuracy)

# Initialize arrays to store results
x_values = np.zeros((len(r_values), num_to_plot))

# Iterate over r values
for i, r in enumerate(r_values):
    x = 0.5  # Initial condition
    # Discard transients
    for k in range(reps - 1):
        x = logistic_map(x, r)
    # Store long-term behavior
    for j in range(num_to_plot):
        x = logistic_map(x, r)
        x_values[i, j] = x

# Plot the bifurcation diagram

for i in range(len(r_values)):
    plt.plot([r_values[i]] * num_to_plot, x_values[i, :], 'b.', markersize=0.02)

plt.xlabel('Growth Rate (r)')
plt.ylabel('Population (x)')
plt.title('Bifurcation Diagram of the Logistic Map')
plt.xlim(r_min, r_max)
plt.ylim(0, 1)
plt.axis('equal')
plt.grid()
plt.show()

