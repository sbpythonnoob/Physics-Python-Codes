import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
g = 9.81
l = 21
a = (g/l)


def shm(y,t):
    theta, omega = y
    dydt = [omega, -a * np.sin(theta)]
    return dydt

y0 =0.2*np.pi,1.2
omega = 0
t = np.linspace(0,10,1000)
solve = odeint(shm,y0,t)
plt.plot(solve[:,0],solve[:,1])
plt.show()




