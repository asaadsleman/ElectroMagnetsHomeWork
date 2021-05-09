import matplotlib.pyplot as plt
import numpy as np

global d
d = 2*pow(10,-6)

global kq
kq = 144.0

#~~~~~Part A~~~~~
def electricFieldConstant():
    x, y = np.meshgrid(np.arange(-10, 10, 1), np.arange(-10, 10, 1))
    u, v = 0, 10

    fig, ax = plt.subplots()
    ax.quiver(x, y, u, v)
    plt.show()
    

def elctricFieldOfPointCharge(x, y, a=0, b=0):
    x = x - a
    y = y - b
    theta = np.arctan2(y, x)

    try:
        baseVal = kq / (x ** 2 + y ** 2)
    except ZeroDivisionError:
        baseVal = 0

    xVal = baseVal * np.cos(theta)
    yVal = baseVal * np.sin(theta)

    return [xVal, yVal]


def electricFieldQuiverForPointCharge(a=0, b=0):
    x, y = np.meshgrid(np.arange(a-1, a+1, 0.08), np.arange(b-1, b+1, 0.08))
    u, v = elctricFieldOfPointCharge(x, y, a, b)
    fig, ax = plt.subplots()
    ax.quiver(x, y, u, v)

    pot = kq / (((x-a) ** 2 + (y-b) ** 2) ** 0.5)
    ax.contour(x, y, pot)

    plt.show()




#~~~~~Part B~~~~~
def electricFieldOfDipole(x, y, a1, b1, a2, b2):
    v1 = elctricFieldOfPointCharge(x,y,a1,b1)
    v2 = elctricFieldOfPointCharge(x,y,a2,b2)
    v3 = [[0 for i in range(len(v1[0]))] for j in range(len(v1))]
    
    for i in range(len(v1)):
        for j in range(len(v1[i])):
            v3[i][j] = v1[i][j]-v2[i][j]

    return v3

    
    
def ElectricFieldQuiverForDipole():
    jump = d/8
    
    x, y = np.meshgrid(np.arange(-2*d, 2*d, jump), np.arange(-2*d, 2*d, jump))
    u, v = electricFieldOfDipole(x, y, 0, -d/2, 0, d/2)
    fig, ax = plt.subplots()
    ax.quiver(x, y, u, v,scale=pow(10,16))
    

    pot = ElectricPotentialOfDipole(y,x)
    ax.contour(x, y, pot)
    
    plt.show()


def ElectricPotentialOfDipole(r, x=0):
    w1 = 1/(x**2+(r+d/2)**2)
    w2 = 1/(x**2+(r-d/2)**2)
    w = w1-w2
    return kq*w


def ElectricPotentialOfPointCharge(r):
    try:
        return  (kq / np.abs(r))
    
    except ZeroDivisionError():
        return 1000
    

def plotOfPotentials():
    x = np.linspace(-10,10,100)
    y1 = ElectricPotentialOfPointCharge(x)
    y2 = ElectricPotentialOfDipole(x)
    
    plt.plot(x, y1, label="Point charge")
    plt.plot(x, y2, label="Dipole")
    plt.legend()
    plt.show()
    
    
    
    
#~~~~~Part C~~~~~
def ElectricFieldForMirrorCharges(x,y):
    w1 = x-d
    w2 = y-d
    w3 = x+d
    w4 = y+d

    r1 = pow((w1**2)+(w2**2),3/2)
    r2 = pow((w1**2)+(w4**2),3/2)
    r3 = pow((w3**2)+(w4**2),3/2)
    r4 = pow((w3**2)+(w2**2),3/2)

    sizeX = (w1/r1)-(w1/r2)+(w3/r3)-(w3/r4)
    sizeY = (w2/r1)-(w4/r2)+(w4/r3)-(w2/r4)

    return (kq*sizeX,kq*sizeY)


def ElectricFieldQuiverForMirrorCharges():
    jump = d/15
    
    x, y = np.meshgrid(np.arange(0, 3*d, jump), np.arange(0, 3*d, jump))
    u, v = ElectricFieldForMirrorCharges(x, y)
    fig, ax = plt.subplots()
    ax.quiver(x, y, u, v)
    
    plt.show()
    
    
def ElectricPotentialCalculator(y):
    eps0 = 8.845e-12
    z = np.gradient(ElectricFieldForMirrorCharges(0, y))
    sum = 0
    for i in range(len(z)):
        z[i] = z[i] * eps0
        sum+=z[i]
    return sum


def ElectricFieldPlotForDensity():

    x, y = np.linspace(0, 3*d, 100), np.linspace(0,3*d,100)
    u = ElectricPotentialCalculator(x)
    plt.plot(x, y, u)

    plt.show()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def runPartA():
    electricFieldConstant()
    electricFieldQuiverForPointCharge()
    electricFieldQuiverForPointCharge(2,8)

def runPartB():
    ElectricFieldQuiverForDipole()
    plotOfPotentials()
    
def runPartC():
    #ElectricFieldQuiverForMirrorCharges()
    ElectricFieldPlotForDensity()

#runPartA()
#runPartB()
runPartC()