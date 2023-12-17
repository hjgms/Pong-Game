import pygame as pg


class Object:
    def __init__(self):
        self.posY = 100
        self.posX = 300
        self.w = 15
        self.h = 15
        self.directionY = -1
        self.directionX = -1
        self.color = "#3661E0"

    def draw_object(self, surface):
        self.posY += self.directionY
        self.posX += self.directionX

        pg.draw.rect(surface, self.color, (self.posX, self.posY, self.w, self.h))

    def collision(self, game):
        if self.posY == 0:
            self.directionY = 1
        if self.posY + self.h == game.HEIGHT:
            self.directionY = -1
        if self.posX == 0:
            game.set_point(2)
        if self.posX + self.w == game.WIDTH:
            game.set_point(1)

        # collision in players

        down_player1 = (game.player1.posY + game.player1.h)
        width_player1 = (game.player1.posX + game.player1.w)
        down_player2 = (game.player2.posY + game.player2.h)
        width_player2 = (game.player2.posX + game.player2.w)

        down_obj = (self.posY + self.h)
        width_obj = (self.posX + self.w)

        # front faces collision
        if width_player1 == self.posX and (game.player1.posY <= self.posY and down_player1 >= down_obj):
            self.directionX = 1
        if game.player2.posX == width_obj and (game.player2.posY <= self.posY and down_player2 >= down_obj):
            self.directionX = -1

        # faces top and down collision
        if (game.player1.posY == down_obj and (game.player1.posX <= self.posX <= width_player1)) or (game.player1.posY == down_obj and width_player1 == self.posX):
            self.directionY = -1
            self.directionX = 1
        if (game.player2.posY == down_obj and (game.player2.posX <= self.posX <= width_player2)) or (game.player2.posY == down_obj and game.player2.posY == width_obj):
            self.directionY = -1
            self.directionX = -1
        if (down_player1 == self.posY and (game.player1.posX <= self.posX <= width_player1)) or (down_player1 == self.posY and width_player1 == self.posX):
            self.directionY = 1
            self.directionX = 1
        if (down_player2 == self.posY and (game.player2.posX <= self.posX <= width_player2)) or (down_player2 == self.posY and game.player2.posX == width_obj):
            self.directionY = 1
            self.directionX = -1
