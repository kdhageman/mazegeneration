import unittest
from maze.maze import Maze, Direction


class MazeTest(unittest.TestCase):
    def test_init(self):
        maze = Maze(2)
        self.assertEqual(maze.dim, 2)
        self.assertEqual(maze.grid.shape, (3, 3))

    def test_get(self):
        maze = Maze(2)
        maze.grid[1, 0].visited = True
        self.assertEqual(maze.get(0, 0).visited, False)
        self.assertEqual(maze.get(1, 0).visited, True)

    def test_connect_east(self):
        maze = Maze(2)
        maze.connect(0, 0, Direction.EAST)
        self.assertEqual(maze.get(0, 0).walls[Direction.EAST], False)
        self.assertEqual(maze.get(1, 0).walls[Direction.WEST], False)

    def test_connect_south(self):
        maze = Maze(2)
        maze.connect(0, 0, Direction.SOUTH)
        self.assertEqual(maze.get(0, 0).walls[Direction.SOUTH], False)
        self.assertEqual(maze.get(0, 1).walls[Direction.NORTH], False)

if __name__ == '__main__':
    unittest.main()
