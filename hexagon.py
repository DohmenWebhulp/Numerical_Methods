import pygame as pg
import numpy as np

def calc_p(ab, be, db, de, n=1):
    bc = (ab * be)/db
    ac = (bc * de)/be
    p_lower = 6 * n * be
    p_upper = 6 * n * ac
    return p_lower, p_upper

def pyth(x, y):
    return np.sqrt(x**2 + y**2)

pg.init()

clock = pg.time.Clock()
start_time = pg.time.get_ticks()

screen = pg.display.set_mode((600, 600))

s = 100 * np.sqrt(3)
center = (300, 450 - s)
x = 200 * (np.sqrt(3)/3 - 0.5); y = 200 * (1 - np.sqrt(3)/2); z = 200 * np.sqrt((7/3)-(4*np.sqrt(3)/3))
x_1 = (300 - x - z)/2; y_1 = (900 - 3*s - y)/2
p = 400 * np.pi; p_h_1 = 1200; p_h_2 = 8*s
area = 40000 * np.pi; area_h_1 = 600 * s; area_h_2 = 120000 * (1 + z)
p_lower, p_upper = calc_p(1, 1, 0.5 * np.sqrt(3), 0.5)

pg.display.set_caption("Archimedes' zeshoek")

font = pg.font.Font(None, 24)

text_1 = font.render("Welcome to a demonstration of Archimedes' hexagon.", True, "white", )
text_2 = font.render("He used them to approximate the value of pi.", True, "white")
text_3 = font.render("Here is how he did it:", True, "white")
text_4 = font.render("He started with a circle of radius 1.", True, "white")
text_5 = font.render("He then inscribed a hexagon inside. He knew the sides of the hexagon are equal to the radius of the circle, as the hexagon can be made up of 6 equilateral triangles of size 1.", True, "white")
text_6 = font.render("The inner hexagon is for the lower bound on pi. The outer hexagon is for the upper bound.", True, "white")
text_7 = font.render("Let's zoom in on the two similar triangles indicated by the green lines.", True, "white")

text_8 = font.render("We have that DE equals to 0.5, as it is half of the side of the internal hexagon.", True, "white")
text_9 = font.render("As BE equals to 1, it follows from Pythagoras that DB equals to (\u221A3)/2", True, "white")

lines_1 = ["He then inscribed a hexagon inside.", "He knew the sides of the hexagon are equal to the radius of the circle,", "as the hexagon can be made up of 6 equilateral triangles of size 1."]
lines_2 = ["The inner hexagon is for the lower bound on pi.", "The outer hexagon is for the upper bound."]

a = font.render("A", True, "white")
b = font.render("B", True, "white")
c = font.render("C", True, "white")
d = font.render("D", True, "white")
e = font.render("E", True, "white")
ab = font.render("AB = 1", True, "white")
be = font.render("BE = 1", True, "white")
db = font.render("DB = (\u221A3)/2", True, "white")
de = font.render("DE = 1/2", True, "white")

rect_a = a.get_rect(center=(100, 500))
rect_b = b.get_rect(center=(500, 500))
rect_c = c.get_rect(center=(100, 500 - (4*s)/3))
rect_d = d.get_rect(center=(500 - 2*s, 500))
rect_e = e.get_rect(center=(500 - 2*s, 300))
rect_ab = ab.get_rect(center=(300, 520))
rect_be = be.get_rect(center=(500 - s, 400))
rect_db = db.get_rect(center=(325, 480))
rect_de = de.get_rect(center=(520 - 2*s, 400))

rect_1 = text_1.get_rect(center=(300, 300))
rect_2 = text_2.get_rect(center=(300, 300))
rect_3 = text_3.get_rect(center=(300, 300))
rect_4 = text_4.get_rect(center=(300, 300))
#rect_5 = text_5.get_rect(center=(300, 300))
rect_6 = text_6.get_rect(center=(300, 300))
rect_7 = text_7.get_rect(center=(300, 300))
rect_8 = text_8.get_rect(center=(300, 200))
rect_9 = text_9.get_rect(center=(300, 200))

pg.display.flip()
running = True
y_start = 240
line_height = 20
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("black")
    t = pg.time.get_ticks() - start_time
    """
    if t < 28000:
        if 0 < t < 4000:
            screen.blit(text_1, rect_1)
        if 4000 < t < 8000:
            screen.blit(text_2, rect_2)
        if 8000 < t < 12000:
            screen.blit(text_3, rect_3)
        if t > 12000:
            pg.draw.aacircle(screen, "blue", center, 200, 1)
            if t < 16000:
                screen.blit(text_4, rect_4)
        if t > 16000:
            pg.draw.polygon(screen, "red", [(400, 450), (200, 450), (100, 450 - s), (200, 450 - 2*s), (400, 450 - 2*s), (500, 450 - s)], 1)
            if t < 20000:
                for i, line in enumerate(lines_1):
                    text = font.render(line, True, "white")
                    rect = text.get_rect(center=(300, y_start + i * line_height))
                    screen.blit(text, rect)
        if t > 20000:
            pg.draw.polygon(screen, "red", [(400 + x, 450 + y), (200 - x, 450 + y), (100 - z, 450 - s), (200 - x, 450 - 2*s - y), (400 + x, 450 - 2*s - y), (500 + z, 450 - s)], 1)
            if t < 24000:
                for i, line in enumerate(lines_2):
                    text = font.render(line, True, "white")
                    rect = text.get_rect(center=(300, y_start + i * line_height))
                    screen.blit(text, rect)
        if t > 24000:
            pg.draw.aaline(screen, "green", center, (200 - x, 450 - 2*s - y), 2)
            pg.draw.aaline(screen, "green", center, (x_1, y_1), 2)
            if t < 28000:
                screen.blit(text_7, rect_7)
                """
    if t > 0:
        if t > 0:
            pg.draw.aaline(screen, "green", (500, 500), (100, 500), 2)
            pg.draw.aaline(screen, "green", (500, 500), (100, 500 - 400 * np.sqrt(3)/3), 2)
            pg.draw.aaline(screen, "green", (100, 500), (100, 500 - 400 * np.sqrt(3)/3), 2)
            pg.draw.aaline(screen, "green", (500 - 200 * np.sqrt(3), 500), (500 - 200 * np.sqrt(3), 300), 2)
            pg.draw.circle(screen, "blue", (500, 500), 400, 1)
            screen.blit(a, rect_a)
            screen.blit(b, rect_b)
            screen.blit(c, rect_c)
            screen.blit(d, rect_d)
            screen.blit(e, rect_e)
        if 2000 < t < 12000:
            screen.blit(text_8, rect_8)
        if t > 2000:
            screen.blit(ab, rect_ab)
            screen.blit(be, rect_be)
            screen.blit(de, rect_de)
        if 14000 < t < 18000:
            screen.blit(text_9, rect_9)
        if t > 14000:
            screen.blit(db, rect_db)
        
    pg.display.flip()

pg.quit()