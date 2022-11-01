# Author: Lydia Delgado Uriarte 
from matplotlib import pyplot as plt

x2= 5
x1 = 0
y2= 3
y1 = 0
dx = x2 - x1
dy = y2 - y1


def lineDrawing(x, y):
    for x in range (x1, x2):
        y = y1 + dy * (x - x1) / dx
        
        plt.plot(x, y, 'bo')
        # Code to add more points
        plt.plot(x+.5, y+.5, 'bo')
        plt.plot(x+1, y+1, 'bo')

lineDrawing(5,4)
plt.show()