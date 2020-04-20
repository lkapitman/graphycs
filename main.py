import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import axes3d

ax = axes3d.Axes3D(plt.figure())

i = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(i, i)
pi = np.pi **2
Z = X * np.sin(X + Y) + Y + pi * 2

ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()
