from random import randrange

from generator.generator import DepthFirstGenerator
from maze.maze import Cell
from render.renderer import Renderer
from solver.solver import DepthFirstSolver
import logging


def main():
    logging.basicConfig(level=logging.DEBUG)

    dim = 50
    maze = DepthFirstGenerator().generate(dim)

    (src, dst, path) = DepthFirstSolver().solve(maze, Cell(0, 0), Cell(dim-1, dim-1))

    Renderer().render(maze, src, dst, path)

if __name__ == "__main__":
    main()
