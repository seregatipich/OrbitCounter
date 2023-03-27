import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# Gravitational constant of the Earth (m^3/s^2)
G = 6.67430e-11
M = 5.97219e24

# ISS orbit details
a = 6771000  # Major Axis (m)
e = 0.0015   # Orbit eccentricity

# Calculation of orbit parameters
h = np.sqrt(G * M * a * (1 - e**2))
T = 2 * np.pi * np.sqrt(a**3 / (G * M))

# Equation of motion
def orbit(y):
    x, y, z, vx, vy, vz = y
    r = np.sqrt(x**2 + y**2 + z**2)
    return [
        vx,
        vy,
        vz,
        -G * M * x / r**3,
        -G * M * y / r**3,
        -G * M * z / r**3,
    ]


# Initial conditions
r0 = a * (1 - e)
v0 = h / r0

# Initial values (x, y, z, vx, vy, vz)
initial_conditions = [r0, 0, 0, 0, v0, 0]

# Solving a system of differential equations
sol = solve_ivp(orbit, (0, T), initial_conditions, rtol=1e-8,
                atol=1e-8, t_eval=np.linspace(0, T, 1000))

# Create 3D graphics
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Adding Earth to the graph
earth_radius = 6371000
u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
x = earth_radius * np.cos(u) * np.sin(v)
y = earth_radius * np.sin(u) * np.sin(v)
z = earth_radius * np.cos(v)
ax.plot_surface(x, y, z, color='blue', alpha=0.3)

# Adding the ISS orbit
ax.plot(sol.y[0], sol.y[1], sol.y[2], label='ISS Orbit')

ax.set_xlabel('X (м)')
ax.set_ylabel('Y (м)')
ax.set_zlabel('Z (м)')
ax.set_title('ISS Orbit 3D')
ax.legend()
plt.show()
