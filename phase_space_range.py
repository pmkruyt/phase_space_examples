# Import the necessary modules and libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Set the initial position and velocity of the particle
x0 = 1
v0 = 1

# Set the time step and the total time of the simulation
dt = 0.01
t_max = 100

# Set the mass, the spring constant, and the friction coefficient of the system
m = 1
k = 1
c = 0.1

# Set the range of velocities over which the particle will be kicked
v_min = 1
v_max = 1.5

# Compute the acceleration of the particle
def acceleration(x, v):
    if v_min <= v <= v_max:
        return -k*x/m - 2*np.sign(v)
    else:
        return -k*x/m 

# Initialize the arrays for the positions and velocities
x = [x0]
v = [v0]

# Simulate the motion of the particle
for t in np.arange(0, t_max, dt):
    a = acceleration(x[-1], v[-1])
    x.append(x[-1] + v[-1]*dt)
    v.append(v[-1] + a*dt)

# Set the figure and the axes for the animation
fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

# Initialize the animation
def init():
    line.set_data([], [])
    return line,

# Define the animation function
def animate(i):
    line.set_data(x[:i], v[:i])
    return line,


# Add axes labels and a title
ax.set_xlabel("Position")
ax.set_ylabel("Velocity")
ax.set_title("Phase Space Trajectory of a Particle in a Spring-Mass System")

# Create the animation
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(x), interval=2, blit=True)

# Show the animation
plt.show()
