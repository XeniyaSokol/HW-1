import matplotlib.pyplot as plt
import numpy as np

from pylab import*
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax= Axes3D (fig)
x= np.arange (-100, 100, 1)
y= np.arange (-100, 100, 1)
x, y= np.meshgrid (x, y)
z= x + y
z1= x +y + 200
ax.plot_surface (x, y, z)
ax.plot_surface (x, y, z1)

ax.scatter (0, 0, 0, 'z', 50)
ax.scatter (0, 0, 0, 'z1', 50)
show( )