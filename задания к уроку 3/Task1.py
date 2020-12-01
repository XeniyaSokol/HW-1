#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import math

#a= int(input())
#k= int(input())
#b= int(input())
a1=1
b1=1
k1=1

a2=2
b2=3
k2=4

a3=5
b3=10
k3=7

x=[]
y1=[]
y2=[]
y3=[]

for i in range (100):
    x_=i/10
    x.append(x_)
    y1.append(k1*math.cos(x_-a1)+b1)
    y2.append(k2*math.cos(x_-a2)+b2)
    y3.append(k3*math.cos(x_-a3)+b3)
    
plt.plot (x, y1)
plt.plot (x, y2)
plt.plot (x, y3)

plt.xlim ([0, 10])
plt.ylim ([-1, 20])