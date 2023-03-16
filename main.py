import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp

# Гравитационная постоянная Земли (м^3/с^2)
G = 6.67430e-11
M = 5.97219e24

# Начальные условия для МКС
a = 6771000  # Большая полуось (м)
e = 0.0015   # Эксцентриситет орбиты

# Параметры орбиты
h = np.sqrt(G * M * a * (1 - e**2))
T = 2 * np.pi * np.sqrt(a**3 / (G * M))

# Уравнения движения
def orbit(t, y):
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

# Начальные условия
r0 = a * (1 - e)
v0 = h / r0

# Начальные значения (x, y, z, vx, vy, vz)
initial_conditions = [r0, 0, 0, 0, v0, 0]

# Решение системы дифференциальных уравнений
sol = solve_ivp(orbit, (0, T), initial_conditions, rtol=1e-8, atol=1e-8, t_eval=np.linspace(0, T, 1000))

# Создание 3D графика
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Добавление Земли на график
earth_radius = 6371000
u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
x = earth_radius * np.cos(u) * np.sin(v)
y = earth_radius * np.sin(u) * np.sin(v)
z = earth_radius * np.cos(v)
ax.plot_surface(x, y, z, color='blue', alpha=0.3)

# Добавление орбиты МКС
ax.plot(sol.y[0], sol.y[1], sol.y[2], label='Орбита МКС')

ax.set_xlabel('X (м)')
ax.set_ylabel('Y (м)')
ax.set_zlabel('Z (м)')
ax.set_title('Орбита МКС и Земля в 3D')
ax.legend()
plt.show()
