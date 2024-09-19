import cv2
import numpy as np
image1 = cv2.imread('asset/image1.png')
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY);
ret, treshold = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2. imshow('Otsu Threshold', treshold)