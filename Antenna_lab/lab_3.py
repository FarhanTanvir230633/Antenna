# Horn Antenna - 3D Radiation Pattern horn antenna


import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, np.pi / 2, 250)
phi = np.linspace(0, 2 * np.pi, 250)

theta, phi = np.meshgrid(theta, phi)

n = 6
R = np.cos(theta) ** n

X = R * np.sin(theta) * np.cos(phi)
Y = R * np.sin(theta) * np.sin(phi)
Z = R * np.cos(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')

ax.set_title("Horn Antenna (3D Radiation Pattern)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_box_aspect((1, 1, 1))

plt.show()
