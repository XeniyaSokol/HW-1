import matplotlib.pyplot as plt
import numpy as np
import math
import sys

print ("vvedite Radius")
R= int(input ())

print ("vvedite alpha v grad  ")
alpha= int(input())
alpha1=math.radians(alpha)

if ((alpha1 <= 0) or (alpha1>np.pi*2)) :
    print ("Error")
    sys.exit()

x= (R*np.cos (alpha1))
y= (R*np.sin (alpha1))

print (round(x))
print (round(y))