import cv2
image = cv2.imread("asset/image2.png")
cv2.imshow("Original Image", image)
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", grayscale)
(th, bw) = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("BW Image", bw)
cv2.waitKey(0)
cv2.destroyAllWindows()