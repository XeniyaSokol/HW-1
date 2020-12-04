#fsolve_1.py
from scipy.optimize import fsolve
from math import exp
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
plt.plot(x, ((x**2)-1))
plt.plot(x, (np.exp(x)+x-1)/x)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-10, 10)
plt.ylim(-2, 40)
plt.grid(True)
plt.show()


def equations(vars):
    x, y = vars
    eq1 = y - (x**2) + 1 
    eq2 = exp(x) + x*(1-y) - 1 
    return [eq1, eq2]

x, y =  fsolve(equations, (-3, -3))

print(round(x, 3), round(y, 3))