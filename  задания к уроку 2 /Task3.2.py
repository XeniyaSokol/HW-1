import numpy as np
from matplotlib import pyplot as plt
from math import pi

u=1.     
v=0.5    
a=2.     
b=0.5   

t = np.linspace(0, 2*pi, 100)
plt.plot( u+a*np.cos(t) , v+b*np.sin(t) )
plt.grid(color='black',linestyle='--')
plt.show()