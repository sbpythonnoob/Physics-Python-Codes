import numpy as np
import scipy.constants as sc 
import matplotlib.pyplot as plt 

hbar = sc.hbar
A = 2
n = 1

def wavefunc(x):
    nc = (2/A)**0.5
    w = nc*np.sin(n*np.pi*x/A)
    return w
x = np.linspace(0,A,200)
psi = wavefunc(x)
plt.figure(figsize=(10,7))
plt.plot(x,psi)
plt.grid(True)
