import matplotlib.pyplot as plt
import numpy as np

def xy(r,phi):
     return r*np.cos(phi), r*np.sin(phi)

fig = plt.figure()
ax = fig.add_subplot(111,aspect='equal',projection='polar')  

phis=np.arange(0,6.28,0.01)
R = 1
# ax.plot( *xy(r,phis), c='r',ls='-' )

theta = np.arange(0, np.pi*2, 0.01)
theta2 = np.arange(0, np.pi/2, 0.01)
#r = 2*R*np.cos(theta)

R = 1 + theta*0
alpha = np.pi/4
P = 2
ax.plot(theta, R, c='r',ls='-' )
ax.plot(theta2, P/np.cos(theta2-alpha), c='r',ls='--' )
ax.set_rmin(0)
ax.set_rmax(4)
ax.set_rticks([0, 1, 2, 3, 4])

plt.show()