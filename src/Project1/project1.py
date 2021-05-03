import matplotlib.pyplot as plt
import numpy as np

#~~~~~Part A~~~~~
def electricFieldPartAa():
    a, b = 2, 8
    x, y = np.meshgrid(np.arange(-10, 10, 1), np.arange(-10, 10, 1))
    
    if (a + b) % 2 == 0:
        u, v = 0, (a+b)
    else:
        u = (a*b*x)/(pow(x, 2) + pow(y, 2))
        v = (a*b*y)/(pow(x, 2) + pow(y, 2))
    
    
    fig, ax = plt.subplots()
    ax.quiver(x, y, u, v)
    plt.show()
    

def elctricFieldPartAe(x,y):
    theta = np.arctan2(y,x)
    
    try:
        baseVal = 144/(x**2+y**2)
    except ZeroDivisionError:
        baseVal = 0 
        
    xVal = baseVal*np.cos(theta)
    yVal = baseVal*np.sin(theta)
    
    return (xVal, yVal)


def elctricFieldPartAeQuiver():
    x, y = np.meshgrid(np.arange(-1, 1, 0.08), np.arange(-1, 1, 0.08))
    u,v = elctricFieldPartAe(x,y)
    fig, ax = plt.subplots()
    ax.quiver(x, y, u, v)
    
    pot = 144/((x**2+y**2)**0.5)
    ax.contour(x,y,pot)
    
    plt.show()


def elctricFieldPartAeDisplaced(z, w):
    x = z - 2
    y = w - 8
    theta = np.arctan2(y, x)

    try:
        baseVal = 144 / (x ** 2 + y ** 2)
    except ZeroDivisionError:
        baseVal = 0

    xVal = baseVal * np.cos(theta)
    yVal = baseVal * np.sin(theta)

    return (xVal, yVal)


def elctricFieldPartAeQuiverDisplaced():
    x, y = np.meshgrid(np.arange(1, 3, 0.08), np.arange(7, 9, 0.08))
    u, v = elctricFieldPartAeDisplaced(x, y)
    fig, ax = plt.subplots()
    ax.quiver(x, y, u, v)

    pot = 144 / (((x-2) ** 2 + (y-8) ** 2) ** 0.5)
    ax.contour(x, y, pot)

    plt.show()

#electricFieldPartAa()
elctricFieldPartAeQuiver()
elctricFieldPartAeQuiverDisplaced()
#elctricFieldPartAHeQuiver()


#~~~~~Part B~~~~~
def ElectricFieldQuiverB():
    x, y = np.meshgrid(np.arange(-10, 10, .2), np.arange(-10, 10, .2))
    r = ((x ** 2 + y ** 2)**0.5)
    fig, ax = plt.subplots()
    q = ax.quiver(x, y, x/(r**3), y/(r**3))
    plt.show()
