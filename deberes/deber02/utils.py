import numpy as np
import math

def divide_image_in_matrix_mxn(img_rgb, dim_rows, dim_cols):
    step_division_height = math.ceil(img_rgb.shape[0]/dim_rows)
    step_division_width = math.ceil(img_rgb.shape[1]/dim_cols)

    new_puzzle_matrix = [[np.array([]) for _ in range(dim_cols)] for _ in range(dim_rows)]

    for i in range(dim_cols):
        for j in range(dim_cols):
            new_puzzle_matrix[i][j] = img_rgb[(i*step_division_height):((i+1)*step_division_height), (j*step_division_width):((j+1)*step_division_width), :]

    return new_puzzle_matrix


def rotate_image_90_degrees(img_rgb):
    m = img_rgb.shape[0]
    n = img_rgb.shape[1]
    roted_image = np.zeros((n, m, 3))

    print(m, n)


    for row in range(m):
        # roted_image[row] = img_rgb[dim_m-1:0]
        print(img_rgb[row, m-1:0, ].shape)
        break

    print(roted_image.shape)

    return roted_image
