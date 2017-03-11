from maze.maze import Maze


class DepthFirstGenerator:
    def generate(self, dim):
        maze = Maze(dim)
        return maze