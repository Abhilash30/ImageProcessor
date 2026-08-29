import numpy as np

KERNELS = {
    "box_blur": np.ones((3, 3)) / 9,

    "gaussian": np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]) / 16,

    "sharpen": np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ]),

    "laplacian": np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ]),

    "sobel_x": np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]),

    "sobel_y": np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])
}
