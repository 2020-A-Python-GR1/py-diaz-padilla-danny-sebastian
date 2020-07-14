from PIL import Image
import numpy as np

import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

# Titulo e icono
pygame.display.set_caption("Mi titulo")


icon = pygame.image.load("fav.ico")
pygame.display.set_icon(icon)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    background_color_rgb = (0, 155, 0)
    screen.fill(background_color_rgb)
    pygame.display.update()



