# House.py

import enum
import pygame

class RoomType(enum.Enum):
    KITCHEN = 1
    GARAGE = 2
    BEDROOM = 3
    COMMON_ROOM = 4

class Room:
    def __init__(self, _room_type):
        self.room_type = _room_type
        self.lights_onoff = False
        self.walls = [[]]

    def render(self, surface, room_origin):
        for wall in self.walls:
            pygame.draw.line(surface, (180, 180, 180), (wall[0].x + room_origin.x, wall[0].y + room_origin.y), (wall[1].x + room_origin.x, wall[1].y + room_origin.y), 10)

class House:
    def __init__(self, rooms):
        self.rooms = rooms

    def render(self, house_origin):
        for room in self.rooms:
            room.render(house_origin)  # TODO: Rooms can't all have the same origin
