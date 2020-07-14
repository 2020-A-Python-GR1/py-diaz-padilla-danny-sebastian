from PIL import Image
import numpy as np

import pygame
import scipy.misc
import matplotlib.pyplot as plt

from utils import divide_image_in_matrix_mxn, rotate_image_90_degrees

image_rgb = scipy.misc.face()  # altoxanchox3  (3 dimensiones RGB)

dimension_m = 2
dimension_n = 2

# puzzle_matrix = divide_image_in_matrix_mxn(image_rgb, dimension_m, dimension_n)
# rotate_image_90_degrees(image_rgb)

plt.imshow(image_rgb[:, :, ::-1])
plt.show()


"""

pygame.init()
screen = pygame.display.set_mode([800, 600])

# Titulo e icono
pygame.display.set_caption("Mi titulo")


animal = pygame.transform.scale(pygame.surfarray.make_surface(image_rgb), (400, 300))

icon = pygame.image.load("fav.ico")
pygame.display.set_icon(icon)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    background_color_rgb = (0, 155, 0)
    screen.fill(background_color_rgb)
    screen.blit(animal, (20, 20))


    pygame.display.update()



"""
