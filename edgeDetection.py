import cv2
img = cv2.imread('asset/image1.png')
t_lower = 50
t_upper =  150
aperture_size = 5
l2gr = True
edge = cv2.Canny(img, t_lower, t_upper)
edgeAppture = cv2.Canny(img, t_lower, t_upper, apertureSize=aperture_size)
edgeL2 = cv2.Canny(img, t_lower, t_upper, L2gradient=l2gr)
cv2.imshow('Edge Default Canny', edge)
cv2.imshow('Edge Aperture Canny', edgeAppture)
cv2.imshow('Edge L2Gradient Canny', edgeL2)