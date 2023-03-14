import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
G = 6.674e-11 # гравитационная постоянная
M_earth = 5.972e24 # масса Земли
R_earth = 6.371e6 # радиус Земли

# Dictionary of bodies
bodies = {
    'ISS': {'mass': 419725, 'height': 408000, 'velocity': 7660},
    'Hubble Space Telescope': {'mass': 11110, 'height': 540000, 'velocity': 7660},
    'Terra': {'mass': 1060, 'height': 705000, 'velocity': 7480},
    'Aqua': {'mass': 1390, 'height': 705000, 'velocity': 7480}
}

# Select a body
body = 'ISS'

# Parameters of the selected body
m = bodies[body]['mass']
h = bodies[body]['height']
v0 = bodies[body]['velocity']

# Координаты тела в начальный момент времени
x0 = R_earth + h
y0 = 0
vx0 = 0
vy0 = v0

# Функция, описывающая движение тела
def motion(state, t):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    ax = -G*M_earth*x/r**3
    ay = -G*M_earth*y/r**3
    return [vx, vy, ax, ay]

# Время моделирования
t = np.linspace(0, 2*3600, 10000)

# Начальные условия
state0 = [x0, y0, vx0, vy0]

# Решаем уравнения движения
state = odeint(motion, state0, t)

# Извлекаем координаты и скорости
x = state[:, 0]
y = state[:, 1]
vx = state[:, 2]
vy = state[:, 3]

# Рисуем траекторию
plt.plot(x/R_earth, y/R_earth)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('x, R_earth')
plt.ylabel('y, R_earth')
plt.title(f'Trajectory of {body}')
plt.show()
