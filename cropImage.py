import cv2
image = cv2.imread("asset/image2.png")
cv2.imshow("Original Image", image)
cropped = image[200:400, 100:600] 
cv2.imshow("Crop Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()