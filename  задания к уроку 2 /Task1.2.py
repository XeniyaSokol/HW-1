import matplotlib.pyplot as plt
import decimal
import numpy as np

x= []
y= []
x1= []
y1= []
for i in range (1, 100, 1):
    x_= i
    x.append (x_)
    y.append ( 1 / x_)
    
for i in range (-100,-1,1):
    x_=i
    x1.append (x_)
    y1.append (1/x_)
    

plt.plot(x, y)
plt.plot (x1, y1)
plt.show()
