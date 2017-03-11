from random import randrange, shuffle
import logging
from maze.maze import Maze, Direction


class DepthFirstGenerator:
    def generate(self, dim):
        self.maze = Maze(dim)

        x = randrange(dim)
        y = randrange(dim)
        logging.debug("Chose (%s, %s) as initial cell", x, y)

        self.stack = [(x, y)]
        self.maze.get(x, y).visited = True

        while len(self.stack) > 0:
            cursearch = self.stack[-1]
            randdirs = self.randdirs()

            foundnext = False
            for dir in randdirs: # search for a new cell to explore
                candidate = self.maze.getbydir(cursearch[0], cursearch[1], dir)
                if candidate is not None and not candidate.visited: # new explorable cell found
                    self.maze.connect(cursearch[0], cursearch[1], dir) # create path between current and new cell
                    candidate.visited = True # set new node as visited
                    self.stack.append((candidate.x, candidate.y))# set new cell as next explorable node
                    foundnext = True
                    break
            if not foundnext:
                self.stack.pop()
        return self.maze

    def randdirs(self):
        result = [0 for x in range(4)]
        randindices = [i for i in range(4)]
        shuffle(randindices)
        for i, dir in enumerate(Direction):
            result[randindices[i]] = dir
        return result