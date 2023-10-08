from DATA.modules.base.frame import Frame
from DATA.modules.base.game import Game
from DATA.modules.base.menu import Menu

from DATA.modules.draw import Draw

from DATA.modules.variables import *
import pygame


class Main:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.play = True
        self.fps = 0

        self.player = 0

        Game.new(self)

        self.frame_stats = Frame(25, 34, [])
        self.frame_stats.create()

        self.frame_message = Frame(75, 9, [])
        self.frame_message.create()

        self.window = []

        self.mouse = [0, 0]

        self.game = [
            Draw(self)
        ]

        self.debug = False

        pygame.display.set_caption(NAME, ICONNAME)

    def start(self):
        while self.play:
            self.fps += 1

            self.player.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.debug = False if self.debug else True

            self.mouse = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_d]:
                self.player.move("right")

            if keys[pygame.K_a]:
                self.player.move("left")

            if keys[pygame.K_w]:
                self.player.move("up")

            if keys[pygame.K_s]:
                self.player.move("down")

            if keys[pygame.K_LCTRL]:
                if not self.player.stats.stamina_was_using:
                    self.player.run = True

                if self.player.stats.stamina_now <= 0:
                    self.player.run = False
                    self.player.stats.stamina_was_using = True
            else:
                self.player.run = False

            for element in self.game:
                element.start()

            if self.fps % 5 == 0:
                self.frame_message.insert = Menu.frame_message(self)
                self.frame_message.create()

                self.frame_stats.insert = Menu.frame_stats(self)
                self.frame_stats.create()

            self.clock.tick(FPS)

        Game.save(self)

        pygame.quit()
