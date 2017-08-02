import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from mpl_toolkits.mplot3d import Axes3D
import math


left_lane=open("left_lane.txt",'w')
right_lane = open("right_lane.txt",'w')
ll_sparse=open("ll_sparse.txt",'w')
rl_sparse = open("rl_sparse.txt",'w')

fig, ax = plt.subplots()
pullData = open("rndf_smooth.txt","r").read()
dataArray = pullData.split('\n')
xar = []
yar = []
for eachLine in dataArray:
    if len(eachLine)>1:
        x1,y1 = eachLine.split(',')
        xar.append(float(x1))
        yar.append(float(y1))
        ax.scatter(x1, y1, c='red',alpha=0.3, edgecolors='none')


def get_parallel_pts(x,y,dist):
    xpl = []
    ypl = []
    for i in range(0,100,2):
        dx = x[i+1] - x[i] #run
        dy = y[i+1] - y[i] #rise
        length = math.hypot(dx,dy)
        px = -(dy/length)*dist
        py = (dx/length)*dist
        xpl.append(x[i]-px)
        ypl.append(y[i]-py)
        xpl.append(x[i+1]-px)
        ypl.append(y[i+1]-py)
    return xpl,ypl


xp,yp = get_parallel_pts(xar, yar, -0.175)

for i in range(0,100):
    ax.scatter(xp[i], yp[i], c='blue',alpha=0.3, edgecolors='none')
    left_lane.write("{0:.2f}".format(round(xp[i],2)))
    left_lane.write(",")
    left_lane.write("{0:.2f}".format(round(yp[i],2)))
    left_lane.write("\n")

for i in range(0,100,2):
    ll_sparse.write("{0:.2f}".format(round((xp[i]+xp[i+1])/2,2)))
    ll_sparse.write(",")
    ll_sparse.write("{0:.2f}".format(round((yp[i]+yp[i+1])/2,2)))
    ll_sparse.write("\n")


######
#right lane

xp,yp = get_parallel_pts(xar, yar, +0.175)

for i in range(0,100):
    ax.scatter(xp[i], yp[i], c='green',alpha=0.3, edgecolors='none')
    right_lane.write("{0:.2f}".format(round(xp[i],2)))
    right_lane.write(",")
    right_lane.write("{0:.2f}".format(round(yp[i],2)))
    right_lane.write("\n")

for i in range(0,100,2):
    rl_sparse.write("{0:.2f}".format(round((xp[i]+xp[i+1])/2,2)))
    rl_sparse.write(",")
    rl_sparse.write("{0:.2f}".format(round((yp[i]+yp[i+1])/2,2)))
    rl_sparse.write("\n")


plt.show()


#file2write.write("{0:.2f}".format(round(float(x1),2)))
#file2write.write(",")
#file2write.write("{0:.2f}".format(round(float(y1),2)))
#file2write.write("\n")
