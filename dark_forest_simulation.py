from civilization import Civilization
from universe import Universe
import matplotlib.pyplot as plt
from matplotlib import animation


def main():
    fraction_malicious = 50
    fraction_exposing = 50

    universe = Universe(30, fraction_malicious, fraction_exposing)
    coordinates = universe.coordinates

    earth = universe.civilizations[0]
    # earth.describe()
    if earth.broadcasts:
        earth.send_broadcast()
        neighbours = universe.find_neighbours(earth)
        for i in range(len(neighbours)):
            print(f'{neighbours[i].name} was found. Malicious = {neighbours[i].malicious}')
            if neighbours[i].malicious:
                print(f'{neighbours[i].name} destroys {earth.name}')
            elif neighbours[i].broadcasts:
                print(f'{neighbours[i].name} says, "Hi Neighbour!"')
            else:
                print(f'{neighbours[i].name} remains silent')

    # print(coordinates)
    create_plt(coordinates)


def create_plt(c):
    def update_radius(i, circle):
        circle.radius = i * 0.5
        return circle
    fig = plt.gcf()
    plt.plot(*zip(*c),marker='o',ls='')
    plt.title("Dark Forest Universe", fontsize=12)
    ax = plt.gca()
    ax.set_facecolor('xkcd:black')
    # print(c[0])
    # circle = plt.Circle((200, 200), 10, ec='y', fc=None)
    # plt.gca().add_patch(circle)
    # anim = animation.FuncAnimation(
    #     fig, update_radius, fargs = (circle,), frames=200, interval=10)
    plt.show()

def create_circle(plt, l):
    x = l[0]
    y = l[1]

    return circle

def update_radius(i, circle):
    circle.radius = i*0.5
    return circle,

def create_animation():
    fig = plt.gcf()
    ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
    ax.set_aspect('equal')
    circle = create_circle()
    ax.add_patch(circle)
    anim = animation.FuncAnimation(
        fig, update_radius, fargs = (circle,), frames=30, interval=50)
    plt.title('Simple Circle Animation')
    plt.show()

if __name__ == '__main__':
    main()