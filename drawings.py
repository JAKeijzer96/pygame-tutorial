import pygame as pg
from sys import exit

pg.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_display = pg.display.set_mode((800, 600))

game_display.fill(BLUE)

pix = pg.PixelArray(game_display)
pix[10][10] = GREEN

pg.draw.line(game_display, RED, (200, 300), (700, 500), 5)

pg.draw.circle(game_display, RED, (100, 100), 100)

pg.draw.rect(game_display, GREEN, (150, 150, 200, 100))

pg.draw.polygon(game_display, WHITE, ( (140, 5), (200, 16), (88, 333), (600, 222), (555, 222)  ) )

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()