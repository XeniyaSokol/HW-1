%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,100)
k=5
k1=1
plt.plot(x, np.cos(k*x), x, np.cos(k1*x), marker = 'o')