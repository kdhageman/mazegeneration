import matplotlib.pyplot as plt
import numpy as np

class Renderer:
    def render(self, maze, src, dst, path, interval=None):
        mazearray = maze.toimagearray()

        patharray = np.ones((2 * maze.dim + 1, 2 * maze.dim + 1))
        patharray[2 * src.x + 1, 2 * src.y + 1] = 0 # src point
        # overlay path over maze
        curx, cury = src.x, src.y
        for dir in path:
            patharray[2 * curx + 1 + dir.hor, 2 * cury + 1 + dir.ver] = 0
            patharray[2 * curx + 1 + 2 * dir.hor, 2 * cury + 1 + 2 * dir.ver] = 0
            curx, cury = curx + dir.hor, cury + dir.ver
        patharray[2 * dst.x + 1, 2 * dst.y + 1] = 0 # dst point

        # customer color map
        cmap = plt.cm.gray
        cmap.set_under(color='white', alpha="0")

        # plot image
        plt.imshow(mazearray.T[::1])
        plt.gray()
        plt.imshow(patharray.T[::1], cmap=cmap, alpha=0.75)
        plt.title("{}x{}".format(maze.dim, maze.dim))
        if interval is None:
            plt.show()
        else:
            plt.pause(interval)