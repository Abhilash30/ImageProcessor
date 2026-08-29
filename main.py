from PIL import Image
import numpy as np
from image_processor.convolution import Manualconvolution
from image_processor.filters import KERNELS
from image_processor.scipy_filters import scipy_convolution
from scipy import ndimage
import time

im = Image.open("images/testimg.jpg");
fade = Image.open("images/fadeout.jpeg");
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

def masking():
    image_array = image_array.astype(np.float32)
    fade_array = fade_array.astype(np.float32)
    image_array = np.multiply(image_array, 0.0005*fade_array)
    image_array = image_array.astype(np.uint8)
    output = Image.fromarray(image_array)
    output.show()


def invert():
    image_array  = np.asarray(im);
    inverted = 255 - image_array
    output = Image.fromarray(inverted)
    output.show()

def grayscale():
    image_array  = np.asarray(im);
    image_array = image_array.astype(np.float32)
    red = image_array[:, :, 0]
    green = image_array[:,:,1]
    blue = image_array[:,:,2]

    gray = (0.299*red + 0.587*green + 0.114*blue)
    gray = np.clip(gray, 0, 255);
    gray = gray.astype(np.uint8)
    output = Image.fromarray(gray)
    output.show()

def Getgrayscale():
    image_array  = np.asarray(im);
    image_array = image_array.astype(np.float32)
    red = image_array[:, :, 0]
    green = image_array[:,:,1]
    blue = image_array[:,:,2]

    gray = (0.299*red + 0.587*green + 0.114*blue)
    gray = np.clip(gray, 0, 255);
    gray = gray.astype(np.uint8)
    return gray

def brightness(val):
    brightness = gray + val
    output = Image.fromarray(brightness)
    output.show()

def binaryimg():
    binary = gray>128
    output = Image.fromarray(binary)
    output.show()


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

#matrix = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])

    

def main():

    gray = Getgrayscale().astype(np.float32)

    

    

    start = time.perf_counter()
    m = Manualconvolution(gray, KERNELS["box_blur"])
    manual_time = time.perf_counter() - start


    start = time.perf_counter()
    s = scipy_convolution(gray, KERNELS["box_blur"])
    scipy_time = time.perf_counter() - start


    print("Manual:", manual_time)
    print("SciPy:", scipy_time)

if __name__ == "__main__":
    main()
