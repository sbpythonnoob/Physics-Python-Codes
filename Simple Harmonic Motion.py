import numpy as np
import matplotlib.pyplot as plt

n = float(input("Give me the frequency: "))
omega = 2 * np.pi * n
k = float(input("Give me the Spring Constant: "))
t = np.linspace(0,1,100)
A = int(input("Give me the amplitude: "))
phi = np.pi/6
x = A*np.sin(omega*t + phi)
F = - k * x

plt.plot(t,F,linestyle='--', color="red", linewidth = '0.5')
plt.title("SHM")
plt.xlabel("Time")
plt.ylabel("Force")
plt.grid()







