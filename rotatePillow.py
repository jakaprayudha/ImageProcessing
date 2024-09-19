from PIL import Image
image = Image.open("asset/image2.png")
rotate_image = image.rotate(45, fillcolor='#fff')
rotate_image.save('output-pillow.jpg')
