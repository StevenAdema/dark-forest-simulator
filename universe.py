import random
from civilization import Civilization
import matplotlib.pyplot as plt
from scipy import spatial
import numpy as np
from sklearn.neighbors import NearestNeighbors

class Universe:
    def __init__(self, civ_total, malicious, exposing, x=1000, y=1000):
        self.civ_total = civ_total
        self.malicious = malicious
        self.exposing = exposing
        self.x = x
        self.y = y

        self.civilizations = self.generate_civilizations()
        self.coordinates = self.get_civilization_coordinates()
        self.malicious_civs = []
        self.benevolent_civs = []
        self.find_malicious_civilizations()


    def generate_civilizations(self):
        l = []
        for i in range(self.civ_total):
            m = random.randrange(100) < self.malicious
            e = random.randrange(100) < self.exposing
            l.append(Civilization(m, e, grid_size=1000))
        return l


    def get_civilization_coordinates(self):
        coordinates = []
        for i in self.civilizations:
            coordinates.append(i.location)
        return coordinates


    def find_neighbours(self, civ):
        """
        Find the 10 closest neighbours to a civilization
        :param civ: the civilization whose neighbours you'd like to find
        :return: an array civiilzations closest to the passed civ
        """
        neighbours = []
        a = spatial.KDTree(self.coordinates)
        a = a.query(civ.location, k=10)
        for i in np.nditer(a[1]):
            neighbours.append(self.civilizations[i])
        return neighbours


    def find_malicious_civilizations(self):
        for i in self.civilizations:
            if i.malicious:
                self.malicious_civs.append(i.location)
            else:
                self.benevolent_civs.append(i.location)

    def get_civ_by_location(self, location):
        print(self.civilizations)
        # return civ