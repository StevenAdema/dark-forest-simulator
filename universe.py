import random
from civilization import Civilization
import matplotlib.pyplot as plt
from scipy import spatial
from sklearn.neighbors import NearestNeighbors

class Universe:
    def __init__(self, civ_total, malicious, exposing):
        self.civ_total = civ_total
        self.malicious = malicious
        self.exposing = exposing

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
            l.append(Civilization(m, e))
        return l


    def get_civilization_coordinates(self):
        coordinates = []
        for i in self.civilizations:
            coordinates.append(i.location)
        return coordinates


    def find_nearest_neighbours(self, civ):
        a = spatial.KDTree(self.coordinates)
        print('earth location', civ.location)
        a = a.query(civ.location, k=8)
        print(a)
        print(a[1][1])
        print(self.coordinates[a[1][1]])


    def find_malicious_civilizations(self):
        for i in self.civilizations:
            if i.malicious:
                self.malicious_civs.append(i.location)
            else:
                self.benevolent_civs.append(i.location)