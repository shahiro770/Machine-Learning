# Person.py

import enum
import pygame

class Direction(enum.Enum):
    NONE_X = -2
    NONE_Y = -1
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Person:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.accel = 8
        self.speed_x = 0
        self.speed_y = 0
        self.max_speed = 15

    def updatePos(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def updateSpd(self, direction):  # TODO: Check for wall collisions
        if direction == Direction.UP:
            if abs(self.speed_y - self.accel) <= self.max_speed:
                self.speed_y -= self.accel
        elif direction == Direction.RIGHT:
            if abs(self.speed_x + self.accel) <= self.max_speed:
                self.speed_x += self.accel
        elif direction == Direction.DOWN:
            if abs(self.speed_y + self.accel) <= self.max_speed:
                self.speed_y += self.accel
        elif direction == Direction.LEFT:
            if abs(self.speed_x - self.accel) <= self.max_speed:
                self.speed_x -= self.accel
        elif direction == Direction.NONE_X:
            if self.speed_x != 0:
                self.speed_x += self.accel * -(self.speed_x / abs(self.speed_x))
        elif direction == Direction.NONE_Y:
            if self.speed_y != 0:
                self.speed_y += self.accel * -(self.speed_y / abs(self.speed_y))

    def move(self, pressed):
        if not pressed[pygame.K_a] and not pressed[pygame.K_d]:
            self.updateSpd(Direction.NONE_X)
        if not pressed[pygame.K_w] and not pressed[pygame.K_s]:
            self.updateSpd(Direction.NONE_Y)
        if pressed[pygame.K_w]:
            self.updateSpd(Direction.UP)
        if pressed[pygame.K_d]:
            self.updateSpd(Direction.RIGHT)
        if pressed[pygame.K_s]:
            self.updateSpd(Direction.DOWN)
        if pressed[pygame.K_a]:
            self.updateSpd(Direction.LEFT)

    def render(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.getPos(), 26)

    def getPos(self):
        return (int(self.x), int(self.y))
