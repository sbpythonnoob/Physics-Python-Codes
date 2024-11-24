#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:46:42 2024

@author: alzaffer
"""

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate Malus' Law
def malus_law(theta, theta_p):
  
    return np.cos(theta - theta_p)**2

# Generate an array of angles from 0 to 2π
theta = np.linspace(0, 2*np.pi, 30)

# Choose a fixed angle for the polarizer
theta_p = np.pi / 4  # 45 degrees

# Calculate the transmitted intensity
I_Max = float(input("Give me the value of Max Intensity in micro ampere: "))
intensity = I_Max * malus_law(theta, theta_p)

# Plot the result
plt.plot(theta, intensity)
plt.xlabel('Angle (radians)')
plt.ylabel('Transmitted Intensity')
plt.title('Malus\' Law')
plt.grid(True)
plt.show()

