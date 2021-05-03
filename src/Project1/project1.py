import matplotlib.pyplot as plt
import numpy as np

#Part A
a, b = 2, 8
x, y = np.meshgrid(np.arange(-10, 10, 1), np.arange(-10, 10, 1))

if (a + b) % 2 == 0:
    u, v = 0, (a+b)
else:
    u = (a*b*x)/(pow(x, 2) + pow(y, 2))
    v = (a*b*y)/(pow(x, 2) + pow(y, 2))


fig, ax = plt.subplots()
q = ax.quiver(x, y, u, v)
plt.show()


def elctricFieldInD(x,y):
    if (x==0 and y==0):
        return (0, 0)
    else:
        if x==0:
            theta = 90
        else:
            theta = np.arctan(y/x)
            
        baseVal = 144/(x**2+y**2)
        xVal = baseVal*np.cos(theta)
        yVal = baseVal*np.sin(theta)
    
    return (xVal, yVal)

#z = (a+b)*y;
#v,u = np.gradient(z)

def ElectricFieldQuiverB():
    x, y = np.meshgrid(np.arange(-10, 10, .2), np.arange(-10, 10, .2))
    r = ((x ** 2 + y ** 2)**0.5)
    fig, ax = plt.subplots()
    q = ax.quiver(x, y, x/(r**3), y/(r**3))
    plt.show()

#Part B
