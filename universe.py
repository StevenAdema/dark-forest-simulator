import numpy as np
import matplotlib.pyplot as plt
import random

grid_size = 100
grid = np.zeros((grid_size, grid_size), int)

for i in range(10):
    x = random.randrange(grid_size)
    y = random.randrange(grid_size)
    grid[x][y] = 1

for i in range(10):
    x = random.randrange(grid_size)
    y = random.randrange(grid_size)
    grid[x][y] = 2

print(grid)

fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
ax.set_title('dark forest universe')
plt.imshow(grid)
ax.set_aspect('equal')

cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.colorbar(orientation='vertical')
plt.show()
