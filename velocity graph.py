import numpy as np
import matplotlib.pyplot as plt

u = float(input("Give me the initial Velocity: "))
a = float(input("Give me the acceleration: "))
t = int(input("Give me the time: "))
T = np.linspace(0,10,t)

def final_velocity(u,a,T):
    v = u + a*T
    return v

v = final_velocity(u, a, t)
plt.plot(T, final_velocity(u, a, T))
plt.title("Time vs Velocity Graph")
plt.xlabel("time(s)")
plt.ylabel("velocity(m/s)")
plt.grid(True)
print("The velocity of the object is: ",v,"m/s")




