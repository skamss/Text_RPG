import numpy as np
from tile import Wall, Floor
import random

# Кімната підземелля

class RectangularRoom:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    @property
    def center(self):
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return center_x, center_y

    @property
    def inner(self):
        inner_x1 = self.x1 + 1
        inner_y1 = self.y1 + 1
        inner_x2 = self.x2 - 1
        inner_y2 = self.y2 - 1
        return (inner_x1, inner_y1), (inner_x2, inner_y2)

    def intersects(self, other):
        return self.x1 <= other.x2 and self.x2 >= other.x1 and self.y1 <= other.y2 and self.y2 >= other.y1

# Карта всього підземелля

class DungeonMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = np.full((width, height), fill_value=Wall(), dtype=object)
        self.rooms: list[RectangularRoom] = []

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

# Створення карти підземелля

dungeon = DungeonMap(100, 100)

