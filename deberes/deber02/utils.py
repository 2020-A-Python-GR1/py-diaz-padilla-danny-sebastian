import numpy as np
import math

def divide_image_in_matrix_mxn(img_rgb, dim_rows, dim_cols):
    step_division_height = math.ceil(img_rgb.shape[0]/dim_rows)
    step_division_width = math.ceil(img_rgb.shape[1]/dim_cols)

    new_puzzle_matrix = [[np.array([]) for _ in range(dim_cols)] for _ in range(dim_rows)]

    for i in range(dim_rows):
        for j in range(dim_cols):
            new_puzzle_matrix[i][j] = img_rgb[(i*step_division_height):((i+1)*step_division_height), (j*step_division_width):((j+1)*step_division_width), :]

    return new_puzzle_matrix

def detect_image_part(x, y, rows, cols, ANCHO, ALTO):
    row = -1
    col = -1

    x_step = ANCHO//cols
    y_step = ALTO//rows

    last_x = 0

    for i, new_x in enumerate(range(x_step, ANCHO+1, x_step)):
        # print("last-new", last_x, new_x)
        if x >= last_x and x <= new_x:
            col = i
            break
        else:
            last_x += x_step

    last_y = 0

    for j, new_y in enumerate(range(y_step, ALTO+1, y_step)):
        # print("last-new", last_x, new_x)
        if y >= last_y and y <= new_y:
            row = j
            break
        else:
            last_y += y_step

    return row, col


def verify_movement(row, col, empty_row, empty_col):
    # solo hay 4 direcciones apartir del espacio en blanco: arriba, derecha, abajo, izquierda
    # se puede mover si se presiono un pedazo en esa dirección

    if empty_row - 1 == row and empty_col == col:  # comprueba arriba
        return True, "abajo"
    elif empty_row + 1 == row and empty_col == col:  # comprueba abajo
        return True, "arriba"
    elif empty_col - 1 == col and empty_row == row:  # comprueba izquierda
        return True, "derecha"
    elif empty_col + 1 == col and empty_row == row:  # comprueba derecha
        return True, "izquierda"
    else:
        return False, "ningun lado"


