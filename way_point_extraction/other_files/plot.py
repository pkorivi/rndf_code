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
            ax.scatter(x1, y1, c=color,alpha=0.3, edgecolors='none')

plot_lane("ll_sparse.txt", 'blue')
plot_lane("rl_sparse.txt",'green')
plot_lane("rndf_smooth.txt",'red')


plt.show()
