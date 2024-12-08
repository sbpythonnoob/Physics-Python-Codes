import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def lorenz(state,t,sigma,beta,rho):
    x,y,z = state
    dx = sigma*(y - x)
    dy = x *(rho - z)-y
    dz = x*y - beta*z
    return [dx ,dy ,dz]

sigma = 10
rho = 28
beta = 8/3
initial_state = [1.0,1.0,1.0]
t = np.linspace(0,50,1000)
solution = odeint(lorenz, initial_state,t, args=(sigma,beta,rho))

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(solution[:,0],solution[:,1],solution[:,2], '--')

