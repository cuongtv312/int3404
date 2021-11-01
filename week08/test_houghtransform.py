import cv2
import numpy as np
import sys

input_file = sys.argv[1]

img = cv2.imread(input_file)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h = gray.shape[0]
w = gray.shape[1]

edges = cv2.Canny(gray, 125, 200, apertureSize=3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
for line in lines:
    rho, theta = line[0]

    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho

    x1 = int(x0 - 2*w*b)
    y1 = int(y0 + 2*h*a)
    x2 = int(x0 + 2*w*b)
    y2 = int(y0 - 2*h*a)

    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)

cv2.imwrite(input_file.split('.')[-0] + '_output.jpg',img)