import numpy as np
from enum import Enum
import logging

class Maze:
    def __init__(self, dim):
        self.dim = dim
        self.grid = self.initGrid()

    def initGrid(self):
        grid = np.empty((3,3), dtype=object)
        for x in range(self.dim):
            for y in range(self.dim):
                grid[x, y] = Cell()
        return grid

    def get(self, xy):
        return self.get(xy[0], xy[1])

    def get(self, x, y):
        return self.grid[x, y]

    def connect(self, xy, dir):
        self.connect(xy[0], xy[1], dir)

    def connect(self, x, y, dir):
        if self.isCell(x, y) and self.isCell(x+dir.hor, y+dir.ver):
            self.grid[x, y].open(dir)
            self.grid[x+dir.hor, y+dir.ver].open(dir.opposite())
        else:
            logging.debug("Failed to connect (%s, %s, %s): not a neighboring cell", x, y, dir.name)

    def isCell(self, x, y):
        return 0 <= x < self.dim and 0 <= y < self.dim

    def __str__(self):
        res = ""
        for y in range(self.dim):
            for x in range(self.dim): # draw maze edges above cells
                cell = self.grid[x, y]
                if cell.walls[Direction.NORTH]:
                    res += "+-"
                else:
                    res += "+ "
            res += "+\n|"
            for x in range(self.dim): # draw maze cells
                cell = self.grid[x, y]
                if cell.visited:
                    res += "X"
                else:
                    res += "O"
                if cell.walls[Direction.EAST]:
                    res += "|"
                else:
                    res += " "
            res += "\n"
        for x in range(self.dim):  # draw last maze edges row
            res += "+-"
        res += "+"
        return res

class Cell:
    def __init__(self):
        self.visited = False
        self.walls = {}
        for dir in Direction:
            self.walls[dir] = True

    def open(self, dir):
        self.walls[dir] = False

class Direction(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def __init__(self, hor, ver):
        self.hor = hor
        self.ver = ver

    def opposite(self):
        if self == Direction.EAST:
            return Direction.WEST
        if self == Direction.WEST:
            return Direction.EAST
        if self == Direction.NORTH:
            return Direction.SOUTH
        if self == Direction.SOUTH:
            return Direction.NORTH

