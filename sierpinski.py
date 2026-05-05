import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

# boom (simpel)
tree_x = [5, 5]
tree_y = [2, 8]

# appel startpositie
x0 = 5
y0 = 8

g = 9.81 * 0.02  # geschaalde zwaartekracht
v0 = 0

def update(t):
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # boom tekenen
    ax.plot(tree_x, tree_y, lw=6, color="brown")
    ax.scatter(5, 8, s=500, color="green")  # bladerkroon

    # vrije val: s = 1/2 g t^2
    y = y0 - 0.5 * g * t**2

    # grond raken
    if y < 1:
        y = 1

    # appel
    ax.scatter(x0, y, s=200, color="red")

    # grond
    ax.plot([0, 10], [1, 1], lw=2, color="black")

ani = FuncAnimation(fig, update, frames=60, interval=80)

plt.show()