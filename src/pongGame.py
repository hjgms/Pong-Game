import pygame as pg
import sys


class Player1:
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

        if keys[pg.K_w] and self.posY > 0:  # top
            self.posY -= self.v

        if keys[pg.K_s] and self.posY + self.h < game.HEIGHT:  # down
            self.posY += self.v


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


class Game:
    def __init__(self):
        pg.init()
        pg.font.init()

        # variables
        self.player1 = None
        self.player2 = None
        self.ball = None
        self.surface = None

        self.RUNNING = False
        self.CLOCK = None
        self.FPS = 0
        self.WINDOW_TITLE = ''
        self.HEIGHT = 0
        self.WIDTH = 0
        self.TUP_DISPLAY = None

        # points
        self.player_1_points = 0
        self.player_2_points = 0

    def start(self):

        self.player1 = Player1()
        self.player2 = Player2()
        self.ball = Object()

        self.config()
        self.set_display()
        self.run()

    def config(self):
        self.RUNNING = True
        self.CLOCK = pg.time.Clock()
        self.FPS = 240
        self.WINDOW_TITLE = 'Pong game - {} X {}'.format(self.player_1_points, self.player_2_points)
        self.HEIGHT = 500
        self.WIDTH = 700
        self.TUP_DISPLAY = (self.WIDTH, self.HEIGHT)

    def set_display(self):
        pg.display.set_mode(self.TUP_DISPLAY)
        pg.display.set_caption(self.WINDOW_TITLE)
        self.surface = pg.display.get_surface()

    def close(self):
        self.RUNNING = False
        pg.quit()
        sys.exit()

    def set_point(self, player):
        if player == 1:
            self.player_1_points += 1
        if player == 2:
            self.player_2_points += 1
        self.start()

    def run(self):
        while self.RUNNING:

            for i in pg.event.get():
                if i.type == pg.QUIT:
                    self.close()

            self.player1.input(self)
            self.player2.input(self)
            self.ball.collision(self)

            self.surface.fill("white", (0, 0, self.WIDTH, self.HEIGHT))

            self.player1.draw_player(self.surface, 0)
            self.player2.draw_player(self.surface, self.WIDTH - self.player2.w)

            self.ball.draw_object(self.surface)

            pg.display.update()
            self.CLOCK.tick(self.FPS)


game = Game()
game.start()
