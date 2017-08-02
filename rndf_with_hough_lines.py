import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math

def draw_lines(img, lines, color=[0, 0, 255], thickness=10):
    """
    Desc:
    """
    for line in lines:
        for x1,y1,x2,y2 in line:
            line_length = math.sqrt((x2-x1)**2+(y2-y1)**2)
            if  line_length < 20 and line_length >8:
                file2write.write(str(x1))
                file2write.write(',')
                file2write.write(str(y1))
                file2write.write(',')
                file2write.write(str(x2))
                file2write.write(',')
                file2write.write(str(y2))
                file2write.write('\n')
                cv2.line(img, (x1, y1), (x2, y2), color, thickness,shift = 0)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.

    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img

def weighted_img(img, initial_img, α=0.8, β=1., λ=0.):
    """
    `img` is the output of the hough_lines(), An image with lines drawn on it.
    Should be a blank image (all black) with lines drawn on it.
    `initial_img` should be the image before any processing.
    The result image is computed as follows:
    initial_img * α + img * β + λ
    NOTE: initial_img and img must be the same shape!
    """
    return cv2.addWeighted(initial_img, α, img, β, λ)

file2write=open("lines.txt",'w')
#reading in an image
image = cv2.imread('Lab_map_400x600.png')
#Flip image to match pixel values to the points published in RVIZ
image = np.flipud(image)
#printing out some stats and plotting
print('This image is:', type(image), 'with dimensions:', image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#Blur if needed
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

# Define our parameters for Canny and apply
low_threshold = 150
high_threshold = 255
#edges = cv2.Canny(np.uint8(gray), low_threshold, high_threshold)
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

#Hough Lines image
rho = 2 # distance resolution in pixels of the Hough grid
theta = np.pi/180 # angular resolution in radians of the Hough grid
threshold = 10     # minimum number of votes (intersections in Hough grid cell)
min_line_len = 10 #minimum number of pixels making up a line
max_line_gap = 10    # maximum gap in pixels between connectable line segments
line_image = hough_lines(edges, rho, theta, threshold, min_line_len, max_line_gap)


# Create a "color" binary image to combine with line image
color_edges = np.dstack((edges, edges, edges))

# Draw the lines on the edge image
final_image = weighted_img(line_image, image, α=0.8, β=1., λ=0.)
#cv2.imwrite("lines.jpg", final_image)
cv2.imshow('lines image',final_image)

#cv2.imshow('image',image)
#cv2.imshow('gray',edges)
k = cv2.waitKey(0)
if k == 27:         # escape to exit
    cv2.destroyAllWindows()
