import matplotlib.pyplot as plt
import numpy as np


a, b = 2, 4


x, y = np.meshgrid(np.arange(-10, 10, 1), np.arange(-10, 10, 1))


if (a + b) % 2 == 0:
    u, v = 0, (a+b)
else:
    u = (a*b*x)/(pow(x, 2) + pow(y, 2))
    v = (a*b*y)/(pow(x, 2) + pow(y, 2))


fig, ax = plt.subplots()
q = ax.quiver(x, y, u, v)
plt.show()


