import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math


image = cv2.imread('Lab_map_400x600.png')
print(type(image))
pullData = open("rndf_smooth.txt","r").read()
dataArray = pullData.split('\n')
for eachLine in dataArray:
    if len(eachLine)>1:
        x1,y1 = eachLine.split(',')
        cv2.circle(image, (600-int(float(x1)*100 + 167),400-int(float(y1)*100 + 42)), radius=1, color=[0,255,0], thickness=1, lineType=8, shift=0)

cv2.imshow('ime',image)
k = cv2.waitKey(0)
if k == 27:         # escape to exit
    cv2.destroyAllWindows()
