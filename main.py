from generator.generator import DepthFirstGenerator
from maze.maze import Maze, Direction
import logging


def main():
    logging.basicConfig(level=logging.DEBUG)

    maze = DepthFirstGenerator().generate(20)
    print(maze)

if __name__ == "__main__":
    main()