#!/usr/bin/env python3

import pygame

SCREEN_X = 640
SCREEN_Y = 480

pygame.init()
pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        # exit()
        break

    print(event)


print("Ferdig") 

