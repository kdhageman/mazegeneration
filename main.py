import sys
import time
from generator.generator import DepthFirstGenerator
from maze.maze import Cell
from render.renderer import Renderer
from solver.solver import DepthFirstSolver
import logging


def main():
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) < 2:
        print("Invalid parameter(s) provided. Usage: main.py <maze_size>")
        sys.exit(-1)
    dim = int(sys.argv[1])

    (maze, passed) = timed(DepthFirstGenerator().generate, dim)
    logging.info("Generation took {:0.3f} seconds".format(passed))

    ((src, dst, path), passed) = timed(DepthFirstSolver().solve, maze, Cell(0, 0), Cell(dim - 1, dim - 1))
    logging.info("Solving took {:0.3f} seconds".format(passed))

    logging.info("Result path is of length {}".format(len(path)))

    Renderer().render(maze, src, dst, path)

def timed(method, *args):
    start_time = time.time()
    result = method(*args)
    return result, time.time() - start_time

if __name__ == "__main__":
    main()
