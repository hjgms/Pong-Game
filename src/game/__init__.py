import pygame as pg
import sys
from player1 import Player1
from player2 import Player2
from object import Object


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
