#!/usr/bin/env python3

import pygame

SCREEN_X = 640
SCREEN_Y = 480
BG_FNAME = "Chapter03/sushiplate.jpg"


pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
background = pygame.image.load(BG_FNAME)

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        # exit()
        break

    screen.blit(background, (0, 0))
    pygame.display.update()

    # print(event)


print("Ferdig") 

