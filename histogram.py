import matplotlib.pyplot  as plt
import cv2
import numpy as np
img = cv2.imaread('asset/image1.png')
B = img[:,:,0] #blue layer
G = img[:,:,1] #green layer
R = img[:,:,2] #red layer
#calculation histogram
b_histogram = cv2.calcHist([img], [0], None, [256], [0,256])
g_histogram = cv2.calcHist([img], [1], None, [256], [0,256])
r_histogram = cv2.calcHist([img], [2], None, [256], [0,256])
#calutaion Equlazation
b_equi = cv2.equalizeHist(B)
g_equi = cv2.equalizeHist(G)
r_equi = cv2.equalizeHist(R)
b_histogram_equi = cv2.calcHist([b_equi], [0], None, [256], [0,256])
g_histogram_equi = cv2.calcHist([g_equi], [1], None, [256], [0,256])
r_histogram_equi = cv2.calcHist([r_equi], [2], None, [256], [0,256])
#visualizing histogram
plt.subplot(2,2,1)
plt.plot(b_histogram, 'b')
plt.subplot(2,2,2)
plt.plot(g_histogram, 'g')
plt.subplot(2,2,3)
plt.plot(r_histogram, 'r')
#visualizing image
cv2.namedWindow('BGR Image', cv2.WINDOW_NORMAL)
cv2.imshow('BGR Image', img)

