# ImageProcessor
Takes an image -> converts it into numbers -> Performs action on numbers -> outputs image

Image -> data
mathematical operations on matrices.
Grayscale - heightxwidth
ColourImages - heightxwidthx3
Possible jobs: Increase/ decrease intensity, image inversion, affect neighbourhood pixels(convolution), Geometric Operations(resize, rotate, crop, flip, translate), feature extraction (edges, corners, blobs, textures)

File Organisation
image_processor/
│
├── main.py
│
├── image/
│   ├── image.py
│   ├── loader.py
│   └── writer.py
│
├── processing/
│   ├── grayscale.py
│   ├── brightness.py
│   ├── threshold.py
│   └── convolution.py
│
├── filters/
│   ├── blur.py
│   ├── sharpen.py
│   └── edge.py
│
├── utils/
│   ├── validation.py
│   └── padding.py
│
└── tests/
    ├── test_image.py
    ├── test_convolution.py
    └── test_filters.py


             ┌───────────────┐
             │ Image Loader  │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │ Image Object  │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │ Processing    │
             │ Engine        │
             └───────┬───────┘
                     ↓
          ┌──────────┼──────────┐
          ↓          ↓          ↓
       Grayscale   Blur       Edge
          │          │          │
          └──────────┼──────────┘
                     ↓
             ┌───────────────┐
             │ Image Writer  │
             └───────────────┘

An image is usually an 8 bit unsigned integer so we have to handle things like clipping overflow underflow conversion

Pillow - loading images
Numpy - convertion to mathematical objects like matrices

Pixelwise operations eg. brightness, inversion, grayscale binary depend only on the input pixel
convolution - depends on surrounding pixels
We use a (heightxwidthx3) matrix, while convolution the kernel is (k_height, k_width, 1(To maintain RGB values of pixels))
padding has four types - 0 padding,

Numpy treats dimentions as axes
kernels - 
