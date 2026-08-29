import numpy as np
from scipy import ndimage


def scipy_convolution(image_array, kernel):
    return ndimage.convolve(
        image_array,
        kernel,
        mode="constant",
        cval=0
    )
