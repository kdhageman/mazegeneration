import logging
from maze.maze import Direction


class DepthFirstSolver:

    def solve(self, maze, src, dst):
        path = []
        curcells = []

        srccell = maze.get(src.x, src.y)
        dstcell = maze.get(dst.x, dst.y)

        srccell.visited = True
        curcells.append(srccell)

        numsteps = 0

        while curcells[-1] is not dstcell:
            cursearch = curcells[-1]
            randdirs = Direction.randdirs()

            foundnext = False
            for dir in randdirs:
                candidate = maze.getbydir(cursearch.x, cursearch.y, dir)
                if candidate is not None and not candidate.visited and not cursearch.walls[dir]: # new explorable cell found
                    path.append(dir)
                    curcells.append(candidate)
                    candidate.visited = True
                    foundnext = True
                    numsteps += 1
                    break
            if not foundnext:
                path.pop()
                curcells.pop()
        logging.info("Maze solving took %d steps", numsteps)

        return src, dst, path

class EmptySolver:

    def solve(self, maze, src, dst):
        return src, dst, []