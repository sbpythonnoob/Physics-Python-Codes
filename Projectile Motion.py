#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:13:37 2024

@author: alzaffer
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Function to calculate the trajectory
g = 9.81 #Gravity
def calculate_trajectory(u, theta, g):
    # Convert angle to radians
    theta_rad = math.radians(alpha)
    
    # Calculate time of flight
    t_flight = 2 * u * math.sin(theta_rad) / g
    
    # Generate time array
    t = np.linspace(0, t_flight, 100)
    
    # Calculate x and y coordinates
    x = u * math.cos(theta_rad) * t
    y = u * math.sin(theta_rad) * t - 0.5 * g * t**2
    
    return x, y, t_flight

# Get user input
u = float(input("Enter the initial velocity (m/s): "))
alpha = float(input("Enter the launch angle (degrees): "))

# Calculate the trajectory
x, y, t_flight = calculate_trajectory(u, alpha)

# Plot the trajectory
plt.plot(x, y)
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Height (m)')
plt.title('Projectile Motion Trajectory')
plt.grid(True)
plt.show()
