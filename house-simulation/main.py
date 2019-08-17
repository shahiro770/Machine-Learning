# main.py

from House import *
from Person import *

import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 900))
pygame.display.set_caption("House simulation")
clock = pygame.time.Clock()

person = Person(0, 0)

running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Keyboard inputs
    pressed = pygame.key.get_pressed()

    person.move(pressed)
    person.render(screen)

    person.updatePos()
    clock.tick()
    pygame.display.flip()