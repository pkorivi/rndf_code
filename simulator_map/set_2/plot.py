import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from mpl_toolkits.mplot3d import Axes3D

fig, ax = plt.subplots()
def plot_lane(lane,color):
    pullData = open(lane,"r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x1,y1 = eachLine.split(',')
            xar.append(float(x1))
            yar.append(float(y1))
            #ax.scatter(x1, y1, c=color,alpha=0.3, edgecolors='none')
        ax.plot(xar, yar, 'k',c=color)

plot_lane("ll.txt", 'blue')
plot_lane("rl.txt",'green')
plot_lane("lane.txt",'red')


plt.show()
