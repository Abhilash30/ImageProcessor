import cv2
from PIL import Image

width = 1600
height = 1600 


path = "img1.jpeg"

image = cv2.imread(path)
print(image.shape)
image = cv2.resize(image, (128, 128))

image = cv2.resize(image,(width, height),interpolation=cv2.INTER_NEAREST)

cv2.imwrite('output_image.png', image)