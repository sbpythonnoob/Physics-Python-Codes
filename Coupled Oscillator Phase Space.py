#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 23:53:40 2025

@author: alzaffer
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def coupled_oscillators(t, state, alpha, beta, delta, gamma, omega, k):
    x1, v1, x2, v2 = state
    
    dx1dt = v1
    dv1dt = -delta * v1 - alpha * x1 - beta * x1**3 + gamma * np.cos(omega * t) + k * (x2 - x1)
    
    dx2dt = v2
    dv2dt = -delta * v2 - alpha * x2 - beta * x2**3 + gamma * np.cos(omega * t) + k * (x1 - x2)
    
    return [dx1dt, dv1dt, dx2dt, dv2dt]

# Parameters
alpha = 1.0
beta = -1.0
delta = 0.2
gamma = 0.3
omega = 1.2
k = 0.1  # Coupling strength

# Initial conditions
initial_state = [0.1, 0.0, -0.1, 0.0]

# Time span
t_span = (0, 100)
t_eval = np.linspace(*t_span, 10000)

# Solve the system
solution = solve_ivp(coupled_oscillators, t_span, initial_state, t_eval=t_eval, args=(alpha, beta, delta, gamma, omega, k))

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(solution.t, solution.y[0], label='x1')
plt.plot(solution.t, solution.y[2], label='x2')
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.legend()
plt.title('Coupled Chaotic Oscillators')
plt.show()

# Phase space plot
plt.figure(figsize=(6, 6))
plt.plot(solution.y[0], solution.y[1], label='Phase space (x1, v1)')
plt.plot(solution.y[2], solution.y[3], label='Phase space (x2, v2)')
plt.xlabel('Position')
plt.ylabel('Velocity')
plt.legend()
plt.title('Phase Space of Coupled Chaotic Oscillators')
plt.show()
