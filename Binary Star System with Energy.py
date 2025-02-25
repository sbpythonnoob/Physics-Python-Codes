#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:44:54 2025

@author: alzaffer
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def binary_star_dynamics(t, y, G, m1, m2):
    x1, y1, vx1, vy1, x2, y2, vx2, vy2 = y
    r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    force = G * m1 * m2 / r**3
    
    ax1 = force * (x2 - x1) / m1
    ay1 = force * (y2 - y1) / m1
    ax2 = -force * (x2 - x1) / m2
    ay2 = -force * (y2 - y1) / m2
    
    return [vx1, vy1, ax1, ay1, vx2, vy2, ax2, ay2]

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
m1 = 2.0e30      # Mass of star 1 (kg)
m2 = 1.0e30      # Mass of star 2 (kg)
a = 1.5e11       # Initial separation (m)

# Initial conditions
x1, y1, vx1, vy1 = -m2 * a / (m1 + m2), 0, 0, 30000
x2, y2, vx2, vy2 = m1 * a / (m1 + m2), 0, 0, -30000
y0 = [x1, y1, vx1, vy1, x2, y2, vx2, vy2]

# Time span
tspan = (0, 3.154e7 * 5)  # Five years in seconds
t_eval = np.linspace(*tspan, 5000)

# Solving the system
solution = solve_ivp(binary_star_dynamics, tspan, y0, t_eval=t_eval, args=(G, m1, m2), method='RK45')

# Extracting results
x1_sol, y1_sol = solution.y[0], solution.y[1]
x2_sol, y2_sol = solution.y[4], solution.y[5]

# Plotting the orbits
plt.figure(figsize=(10, 10))
plt.plot(x1_sol, y1_sol, label='Star 1', color='blue')
plt.plot(x2_sol, y2_sol, label='Star 2', color='red')
plt.scatter([0], [0], color='black', label='Center of Mass', marker='x')
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('Binary Star System - 5 Year Simulation')
plt.legend()
plt.grid()
plt.axis('equal')
plt.show()

# Energy Calculation
kinetic_energy = 0.5 * m1 * (solution.y[2]**2 + solution.y[3]**2) + 0.5 * m2 * (solution.y[6]**2 + solution.y[7]**2)
potential_energy = -G * m1 * m2 / np.sqrt((solution.y[4] - solution.y[0])**2 + (solution.y[5] - solution.y[1])**2)
total_energy = kinetic_energy + potential_energy

# Plotting energy conservation
plt.figure(figsize=(8, 6))
plt.plot(solution.t, total_energy, label='Total Energy', color='purple')
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.title('Energy Conservation in Binary System')
plt.legend()
plt.grid()
plt.show()
