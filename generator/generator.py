from random import randrange
import logging
from maze.maze import Maze, Direction, Cell
import progressbar


class Generator:
    def initbar(self, max):
        self.bar = progressbar.ProgressBar(maxval=max, term_width=30,
                                           widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        self.bar.start()
        self.bar.update(0)

    def updatebar(self, value):
        self.bar.update(value)

    def finishbar(self):
        self.bar.finish()


class DepthFirstGenerator(Generator):
    def generate(self, dim):
        maze = Maze(dim)

        x = randrange(dim)
        y = randrange(dim)
        logging.debug("Chose (%s, %s) as initial cell", x, y)

        stack = [(x, y)]
        maze.get(x, y).visited = True

        self.initbar(dim*dim)
        i = 0
        while len(stack) > 0:
            cursearch = stack[-1]
            randdirs = Direction.randdirs()

            foundnext = False
            for dir in randdirs: # search for a new cell to explore
                candidate = maze.getbydir(cursearch[0], cursearch[1], dir)
                if candidate is not None and not candidate.visited: # new explorable cell found
                    maze.connect(cursearch[0], cursearch[1], dir) # create path between current and new cell
                    candidate.visited = True # set new node as visited
                    stack.append((candidate.x, candidate.y))# set new cell as next explorable node
                    foundnext = True
                    i += 1
                    self.updatebar(i)
                    break
            if not foundnext:
                stack.pop()
        # set all cells as unvisited
        for x in range(dim):
            for y in range(dim):
                maze.get(x, y).visited = False
        self.finishbar()
        return maze


class RandomGenerator(Generator):
    def generate(self, dim):
        maze = Maze(dim)

        x = randrange(dim)
        y = randrange(dim)
        logging.debug("Chose (%s, %s) as initial cell", x, y)

        explorablenodes =[(x, y)]
        maze.get(x, y).visited = True

        self.initbar(dim*dim)
        i = 0
        while len(explorablenodes) > 0:
            cursearch = explorablenodes[randrange(len(explorablenodes))]
            randdirs = Direction.randdirs()

            foundNext = False
            for dir in randdirs: # search for a new cell to explore
                candidate = maze.getbydir(cursearch[0], cursearch[1], dir)
                if candidate is not None and not candidate.visited:
                    maze.connect(cursearch[0], cursearch[1], dir)
                    candidate.visited = True
                    if maze.explorables(candidate.x, candidate.y) > 0:
                        explorablenodes.append((candidate.x, candidate.y))
                    foundNext = True
                    i += 1
                    self.updatebar(i)
                    break
            if not foundNext:
                explorablenodes.remove(cursearch)
        # set all cells as unvisited
        for x in range(dim):
            for y in range(dim):
                maze.get(x, y).visited = False
        self.finishbar()
        return maze

