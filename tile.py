class Tile:
    def __init__(self, walkable, transparent, char, color_in_sight, color_out_sight):
        self.walkable = walkable
        self.transparent = transparent
        self.char = char
        self.color_in_sight = color_in_sight
        self.color_out_sight = color_out_sight

class Wall(Tile):
    def __init__(self):
        super().__init__(walkable=False, transparent=False, char='#',
                         color_in_sight=(210, 210, 210), color_out_sight=(95, 95, 95))

class Floor(Tile):
    def __init__(self):
        super().__init__(walkable=True, transparent=True, char='.',
                         color_in_sight=(120, 120, 120), color_out_sight=(60, 60, 60))
