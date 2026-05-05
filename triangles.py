import numpy as np
#import pygame as pg
import matplotlib.pyplot as plt
"""
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_triangle(surface, center, b):
    h = np.sqrt(3)/2 * b
    
    cx, cy = center
    
    p1 = (cx - b/2, cy + h/3)
    p2 = (cx + b/2, cy + h/3)
    p3 = (cx, cy - 2*h/3)
    
    pygame.draw.polygon(surface, BLACK, [p1, p2, p3], 1)
    return p1, p2, p3
"""
def triangle(b):
    h = np.sqrt(3)/2 * b
    return [
        (0, 2*h/3),
        (-b/2, -h/3),
        (b/2, -h/3),
        (0, 2*h/3),
        (0, -h/3),
    ]

def pyth(h, b):
    x = 0.625 * b - np.pow(h, 2)/ (2 * b)
    y = np.sqrt(0.25 * b * b - x * x)
    u = (np.pow(x, 2) - np.pow(y, 2))/ b + 0.25 * b
    v = np.sqrt(x * x - u * u)
    print(x); print(y)

    h = h - v
    b = b - 2 * u
    return h, b, u, v

h = 0.5 * np.sqrt(3)
b = 1; i = 0
max_iter = 10

pts = triangle(b)
xs, ys = zip(*pts)
print(xs, ys)

while(i < max_iter):
    h_new, b_new, u, v = pyth(h, b)
    xs = xs; ys = [ys, -h/3 + v]
    h = h_new; b = b_new
    i += 1

plt.plot(xs, ys)
plt.axis("equal")
plt.show()
