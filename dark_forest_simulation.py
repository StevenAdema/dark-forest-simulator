import random
from civilization import Civilization
from universe import Universe
import matplotlib.pyplot as plt
from scipy import spatial
from sklearn.neighbors import NearestNeighbors

def main():
    fraction_malicious = 50
    fraction_exposing = 99

    universe = Universe(15, fraction_malicious, fraction_exposing)
    coordinates = universe.coordinates

    earth = universe.civilizations[0]
    if earth.broadcasts:
        earth.send_broadcast()
        neighbours = universe.find_neighbours(earth)


    # print(coordinates)
    plt.scatter(*zip(*coordinates))
    create_plt(plt)
    plt.show()


def create_plt(plt):
    plt.title("Dark Forest Universe", fontsize=12)
    ax = plt.gca()
    ax.set_facecolor('xkcd:black')


if __name__ == '__main__':
    main()