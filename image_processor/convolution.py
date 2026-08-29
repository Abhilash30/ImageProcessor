from PIL import Image
import numpy as np

def Manualconvolution(image_array, kernel):
    original = Image.fromarray(image_array)
    original.show()

    image_array = image_array.astype(np.float32)

    # calculate padding (works for any kernel size, not just 3x3)
    pad_h = (kernel.shape[0] - 1) // 2
    pad_w = (kernel.shape[1] - 1) // 2

    # pad only the spatial dimensions, keep channels (if any) untouched
    if image_array.ndim == 2:
        padded = np.pad(
            image_array,
            ((pad_h, pad_h), (pad_w, pad_w)),
            mode='constant',
            constant_values=0
        )
    else:
        padded = np.pad(
            image_array,
            ((pad_h, pad_h), (pad_w, pad_w), (0, 0)),
            mode='constant',
            constant_values=0
        )

    # calculate the dimensions of the output pixels
    out_v = padded.shape[0] - kernel.shape[0] + 1
    out_h = padded.shape[1] - kernel.shape[1] + 1

    if image_array.ndim == 2:
        output = np.empty((out_v, out_h))
    else:
        output = np.empty((out_v, out_h, image_array.shape[2]))

    # Here each region of the image matrix is broken out and convolution
    # is applied f*g where f and g are the image matrix and the kernel
    for i in range(out_v):
        for j in range(out_h):
            if image_array.ndim == 2:
                region = padded[i:i + kernel.shape[0], j:j + kernel.shape[1]]
                output[i][j] = np.sum(region * kernel)
            else:
                region = padded[i:i + kernel.shape[0], j:j + kernel.shape[1], :]
                output[i][j] = np.sum(region * kernel[:, :, np.newaxis], axis=(0, 1))

    output = np.clip(output, 0, 255)
    # output = (output - output.min()) / (output.max() - output.min())
    # output = output * 255 * 0.25  # NORMALIZATION FOR EDGE DETECTION
    output = output.astype(np.uint8)

    return output
