import random
import string

class Civilization:
    def __init__(self, malicious, broadcasts, progress_time=1000, type=2, grid_size=1000):
        self.grid_size = grid_size
        self.malicious = malicious
        self.type = type
        self.progress_time = progress_time
        self.broadcasts = broadcasts
        self.location = self.generate_location()
        self.name = self.generate_civ_name()

    def generate_location(self):
        x = random.randrange(self.grid_size)
        y = random.randrange(self.grid_size)
        return [x,y]


    def generate_civ_name(self):
        l = random.choice(string.ascii_letters).lower()
        n = str(random.randint(10, 99))
        return 'Civ ' + l + n


    def describe(self):
        print(self.name)
        print('malicious: ', self.malicious)
        print('type: ', self.type)
        print('broadcasts: ', self.broadcasts)
        print('location: ', self.location)

    def send_broadcast(self):
        print('Hello Universe! Anybody there? ')