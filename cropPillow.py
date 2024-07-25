import cv2
from PIL import Image
image = Image.open("asset/image2.png")
image.show()
cropped = (250,250,300,500)
img_crop = image.crop(cropped)
img_crop.show()
