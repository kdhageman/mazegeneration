from generator.generator import DepthFirstGenerator
import logging
import matplotlib.pyplot as plt


def main():
    logging.basicConfig(level=logging.DEBUG)

    maze = DepthFirstGenerator().generate(100)

    render(maze)

def render(maze):
    imagearray = maze.toimagearray()
    plt.imshow(imagearray)
    plt.gray()
    plt.title("100x100 maze")
    plt.show()

if __name__ == "__main__":
    main()