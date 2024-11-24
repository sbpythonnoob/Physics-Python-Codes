import numpy as np
import matplotlib.pyplot as plt
u = float(input("give the Initial Velocity of the Body: "))
a = float(input("Give the acceleration of the body: "))
T = int(input("Give me the time: "))
t = np.linspace(0,10,T)

def displacement(u,t,a):
    S = u*t +0.5 * a * t**2.0
    return S
    
s = displacement(u, T, a) 
plt.plot(t,displacement(u, t, a))
plt.title("Time vs Displacement Graph")
plt.xlabel("Time(s)")
plt.ylabel("Displacement(m)")
plt.grid(True)
print("The Displacement of the pbject is",s,"m")


