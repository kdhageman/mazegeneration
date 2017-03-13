from random import randrange
import logging
from maze.maze import Maze, Direction
import progressbar


class DepthFirstGenerator:
    def generate(self, dim):
        self.maze = Maze(dim)

        x = randrange(dim)
        y = randrange(dim)
        logging.debug("Chose (%s, %s) as initial cell", x, y)

        self.stack = [(x, y)]
        self.maze.get(x, y).visited = True

        self.initbar(dim*dim)
        i = 0
        while len(self.stack) > 0:
            cursearch = self.stack[-1]
            randdirs = Direction.randdirs()

            foundnext = False
            for dir in randdirs: # search for a new cell to explore
                candidate = self.maze.getbydir(cursearch[0], cursearch[1], dir)
                if candidate is not None and not candidate.visited: # new explorable cell found
                    self.maze.connect(cursearch[0], cursearch[1], dir) # create path between current and new cell
                    candidate.visited = True # set new node as visited
                    self.stack.append((candidate.x, candidate.y))# set new cell as next explorable node
                    foundnext = True
                    i += 1
                    self.updatebar(i)
                    break
            if not foundnext:
                self.stack.pop()
        # set all cells as unvisited
        for x in range(dim):
            for y in range(dim):
                self.maze.get(x, y).visited = False
        self.finishbar()
        return self.maze

    def initbar(self, max):
        self.bar = progressbar.ProgressBar(maxval=max, term_width=30, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        self.bar.start()
        self.bar.update(0)

    def updatebar(self, value):
        self.bar.update(value)

    def finishbar(self):
        self.bar.finish()
