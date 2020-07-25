from random import choice, randint
from tkinter import Tk, Canvas
from copy import deepcopy
from PIL import Image, ImageTk
import numpy as np


from utils import divide_image_in_matrix_mxn, detect_image_part, verify_movement

movimientos = 0

ANCHO = 600
ALTO = 600
dim_rows = int(input("Cuantas filas? (debe ser mayor a 1): "))
dim_cols = int(input("Cuantas columnas? (debe ser mayor a 1): "))

assert dim_rows > 1, "El valor de filas debe ser mayor a 1"
assert dim_cols > 1, "El valor de columnas debe ser mayor a 1"
part_to_dissapear_row = randint(0, dim_rows - 1)
part_to_dissapear_col = randint(0, dim_cols - 1)
print("Desaparecerá: ", part_to_dissapear_row, part_to_dissapear_col)

image_directory = "images/one_piece.jpg"

image = Image.open(image_directory)
image = image.resize((ANCHO, ALTO))
image_rgb_array = np.array(image)
image_parts_rgb_array = divide_image_in_matrix_mxn(image_rgb_array, dim_rows, dim_cols)
image_parts = [[None for _ in range(dim_cols)] for _ in range(dim_rows)]
image_parts_original = [[None for _ in range(dim_cols)] for _ in range(dim_rows)]
indexes = [[None for _ in range(dim_cols)] for _ in range(dim_rows)]
# print(image_parts_rgb_array[0][0].shape)


en_juego = True

def click_canvas(event):
    global en_juego, movimientos, canvas, simulation_part_to_dissapear_row, simulation_part_to_dissapear_col

    clicked_row, clicked_col = detect_image_part(event.x, event.y, dim_rows, dim_cols, ANCHO, ALTO)

    can_move, direction = verify_movement(clicked_row, clicked_col, simulation_part_to_dissapear_row, simulation_part_to_dissapear_col)

    print("Posicion clickeada [i][j]", clicked_row, clicked_col)
    print("Se puede mover", can_move)
    print("La pieza pulsada se moverá hacia", direction)
    if can_move and en_juego:
        movimientos += 1
        x1_white = simulation_part_to_dissapear_col*(ANCHO//dim_cols)
        y1_white = simulation_part_to_dissapear_row*(ALTO//dim_rows)
        # x2_white = x1_white + (ANCHO//dim_cols)
        # y2_white = y1_white + ALTO//dim_rows
        # canvas.create_rectangle(x1_white, y1_white, x2_white, y2_white, fill='red', width=0)
        canvas.create_image(x1_white, y1_white, anchor="nw", image=image_parts[clicked_row][clicked_col])


        x1_part = clicked_col*(ANCHO//dim_cols)
        y1_part = clicked_row*(ALTO//dim_rows)
        x2_part = x1_part + (ANCHO//dim_cols)
        y2_part = y1_part + ALTO//dim_rows


        image_part_dissapear = image_parts[simulation_part_to_dissapear_row][simulation_part_to_dissapear_col]
        image_parts[simulation_part_to_dissapear_row][simulation_part_to_dissapear_col] = image_parts[clicked_row][clicked_col]
        image_parts[clicked_row][clicked_col] = image_part_dissapear

        ind = indexes_random[simulation_part_to_dissapear_row][simulation_part_to_dissapear_col]
        indexes_random[simulation_part_to_dissapear_row][simulation_part_to_dissapear_col] = indexes_random[clicked_row][clicked_col]
        indexes_random[clicked_row][clicked_col] = ind

        if indexes == indexes_random:
            canvas.create_image(x1_part, y1_part, anchor="nw", image=image_parts[clicked_row][clicked_col])
            canvas.create_text(200, 20, fill="black",font="Times 25 italic bold",
                        text="Ha completado el juego")
            canvas.create_text(200, 50, fill="black",font="Times 25 italic bold",
                        text="Con " + str(movimientos) + " movimientos")
            en_juego = False
        else:
            canvas.create_rectangle(x1_part, y1_part, x2_part, y2_part, fill='white', width=0)


        simulation_part_to_dissapear_row = clicked_row
        simulation_part_to_dissapear_col = clicked_col


# interfaz
root = Tk()
root.title("Deber 02")
root.resizable(False, False)  # para no redimensionar
root.iconbitmap("fav.ico")
# root.geometry(str(ANCHO) + "x" + str(ALTO))

canvas = Canvas(root, width=ANCHO, height=ALTO)
canvas.bind("<Button-1>", click_canvas)
canvas.pack()



for i in range(dim_rows):
    for j in range(dim_cols):
        image_parts_original[i][j] = ImageTk.PhotoImage(image=Image.fromarray(image_parts_rgb_array[i][j]))
        indexes[i][j] = [i, j]


def get_near_parts(part_to_dissapear_row, part_to_dissapear_col, dim_rows, dim_cols):
    parts = []  # siempre hay min 2 y máximo 4

    last_part = "ninguno"
    if len(parts) > 0:
        last_part = parts[len(parts) - 1]

    if part_to_dissapear_col - 1 >= 0:
        if last_part != "derecha":  # evita bucles inmediatos
            parts.append("izquierda")
    if part_to_dissapear_col + 1 < dim_cols:
        if last_part != "izquierda":  # evita bucles inmediatos
            parts.append("derecha")
    if part_to_dissapear_row - 1 >= 0:
        if last_part != "abajo":  # evita bucles inmediatos
            parts.append("arriba")
    if part_to_dissapear_row + 1 < dim_rows:
        if last_part != "arriba":  # evita bucles inmediatos
            parts.append("abajo")

    return parts


def move_random():
    global indexes_random, dim_rows, dim_cols, simulation_part_to_dissapear_row, simulation_part_to_dissapear_col

    available_part = choice(get_near_parts(simulation_part_to_dissapear_row, simulation_part_to_dissapear_col, dim_rows, dim_cols))

    part_dissapeared = indexes_random[simulation_part_to_dissapear_row][simulation_part_to_dissapear_col]
    if available_part == "arriba":
        indexes_random[simulation_part_to_dissapear_row][simulation_part_to_dissapear_col] = indexes_random[simulation_part_to_dissapear_row-1][simulation_part_to_dissapear_col]
        indexes_random[simulation_part_to_dissapear_row-1][simulation_part_to_dissapear_col] = part_dissapeared
        simulation_part_to_dissapear_row -= 1
    elif available_part == "derecha":
        indexes_random[simulation_part_to_dissapear_row][simulation_part_to_dissapear_col] = indexes_random[simulation_part_to_dissapear_row][simulation_part_to_dissapear_col+1]
        indexes_random[simulation_part_to_dissapear_row][simulation_part_to_dissapear_col+1] = part_dissapeared
        simulation_part_to_dissapear_col += 1
    elif available_part == "abajo":
        indexes_random[simulation_part_to_dissapear_row][simulation_part_to_dissapear_col] = indexes_random[simulation_part_to_dissapear_row+1][simulation_part_to_dissapear_col]
        indexes_random[simulation_part_to_dissapear_row+1][simulation_part_to_dissapear_col] = part_dissapeared
        simulation_part_to_dissapear_row += 1
    elif available_part == "izquierda":
        indexes_random[simulation_part_to_dissapear_row][simulation_part_to_dissapear_col] = indexes_random[simulation_part_to_dissapear_row][simulation_part_to_dissapear_col-1]
        indexes_random[simulation_part_to_dissapear_row][simulation_part_to_dissapear_col-1] = part_dissapeared
        simulation_part_to_dissapear_col -= 1

    print(available_part)


indexes_random = deepcopy(indexes)
simulation_part_to_dissapear_row = deepcopy(part_to_dissapear_row)
simulation_part_to_dissapear_col = deepcopy(part_to_dissapear_col)

is_mixed = False

while not is_mixed:

    for _ in range(10):  # máximo número de movimientos posibles sin repetición
        move_random()

    if indexes != indexes_random:
        is_mixed = True
    else:
        indexes_random = deepcopy(indexes)
        simulation_part_to_dissapear_row = deepcopy(part_to_dissapear_row)
        simulation_part_to_dissapear_col = deepcopy(part_to_dissapear_col)

print(indexes)
print(indexes_random)


for i in range(dim_rows):
    for j in range(dim_cols):

        index = indexes_random[i][j]
        image_parts[i][j] = image_parts_original[index[0]][index[1]]

        if j == simulation_part_to_dissapear_col and i == simulation_part_to_dissapear_row:
            print("No dibujar en la posición (x,y): (", j*(ANCHO//dim_cols), "," , i*(ALTO//dim_rows), ")")
        else:
            print("Dibujando en la posición (x,y): (", j*(ANCHO//dim_cols), "," , i*(ALTO//dim_rows), ")")

            canvas.create_image(j*(ANCHO//dim_cols), i*(ALTO//dim_rows), anchor="nw", image=image_parts[i][j])




root.mainloop()
