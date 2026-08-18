from PIL import Image
import numpy as np


im = Image.open("testimg.jpg");
fade = Image.open("fadeout.jpeg");
fade = fade.resize(im.size)
print(im.format, im.size, im.mode);
print("Pillow image: ", im);
print("Mode ", im.mode);
print("Size ", im.size);

print("Pillow image: ", im)
print("Mode ", im.mode)
print("Size ", im.size)

fade_array = np.asarray(fade);
image_array  = np.asarray(im);

print(fade_array.shape)

image_array = image_array.astype(np.float32)
fade_array = fade_array.astype(np.float32)
image_array = np.multiply(image_array, 0.0005*fade_array)
print(type(image_array))




image_array = image_array.astype(np.uint8)
output = Image.fromarray(image_array)
output.show()



inverted = 255 - image_array
output = Image.fromarray(inverted)

image_array = image_array.astype(np.float32)


red = image_array[:, :, 0]
green = image_array[:,:,1]
blue = image_array[:,:,2]

gray = (0.299*red + 0.587*green + 0.114*blue)
gray = np.clip(gray, 0, 255);
gray = gray.astype(np.uint8)

output = Image.fromarray(gray)


brightness = gray + 10
output = Image.fromarray(brightness)

binary = gray>128
output = Image.fromarray(binary)
print(gray.dtype)


#test = np.array([[(0,255,0), (0, 0,255)], [(0, 0,0), (128,128,128)]])

#test = 255 - test #inversion
#red = test[:,:,0]
#blue = test[:,:,1]
#green = test[:,:,2]

#test = red*0.299 + blue*0.114 + green*0.587
#test = np.clip(test, 0, 255)
#test = test.astype(np.uint8)

#output = Image.fromarray(test)

#output.show()


