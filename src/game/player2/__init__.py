import pygame as pg


class Player2:
    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.h = 128
        self.w = 16
        self.v = 2
        self.color = "#6459FF"

    def draw_player(self, surface, pos=0):
        self.posX = pos
        pg.draw.rect(surface, self.color, (self.posX, self.posY, self.w, self.h))

    def input(self, game):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP] and self.posY > 0:  # top
            self.posY -= self.v

        if keys[pg.K_DOWN] and self.posY + self.h < game.HEIGHT:  # down
            self.posY += self.v
