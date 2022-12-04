import matplotlib.pyplot as plt
import numpy as np

""" xpoints = np.array([0,6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

ypoints = np.array([3,8,1,10])
plt.plot(ypoints, marker='o')
plt.show()

plt.plot(ypoints, 'o:r')
plt.show() """

""" ypoints=np.array([16, 2,47, 25, 3, 27, 68, 95, 34, 50])

plt.plot(ypoints, marker='D', markersize=20, markeredgecolor='cyan', markerfacecolor='hotpink',color='green', linestyle='dotted', linewidth='3')
plt.show() """

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2, ls=':')
plt.show()