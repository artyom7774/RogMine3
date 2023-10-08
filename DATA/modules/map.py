from DATA.modules.entity import Blocks, Block, Entity

from DATA.modules.variables import *
from typing import List
import random


class Map:
    def __init__(self, screen, map: List[List[Block]] = None, generated: bool = False):
        self.screen = screen

        self.generated = generated

        if map is None:
            self.map = [[Blocks.air for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        else:
            self.map = map
            self.initialization()

    def initialization(self):
        for i in range(MAP_HEIGHT):
            for j in range(MAP_WIDTH):
                self.map[j][i] = Block(*self.map[j][i])

    def generate(self):
        if not self.generated:
            blocks = [
                (key, value) for key, value in vars(Blocks).items()
                if isinstance(value, (Block, Entity)) if value.id.find("s") != -1
            ]

            for i in range(MAP_HEIGHT):
                for j in range(MAP_WIDTH):
                    if random.randint(1, 100 / GENERATE_SPAWN_CHANCE) == 1:
                        self.map[j][i] = random.choice(blocks)[1]

    def save(self):
        out = [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

        for i in range(MAP_HEIGHT):
            for j in range(MAP_WIDTH):
                out[j][i] = self.map[j][i].get()

        return out

    def get_screen(self, player_x: int, player_y: int):
        out = self.get_screen_num(player_x, player_y, self.map)

        return out

    @classmethod
    def get_screen_num(cls, player_x: int, player_y: int, game_map: list):
        out = [[Blocks.border] * MAP_VISION_WIDTH for _ in range(MAP_VISION_HEIGHT)]

        for i in range(max(0, player_x - MAP_VISION_WIDTH // 2), min(MAP_WIDTH, player_x + MAP_VISION_WIDTH // 2 + 1)):
            for j in range(max(0, player_y - MAP_VISION_HEIGHT // 2), min(MAP_HEIGHT, player_y + MAP_VISION_HEIGHT // 2 + 1)):
                out[j - player_y + MAP_VISION_HEIGHT // 2][i - player_x + MAP_VISION_WIDTH // 2] = game_map[j][i]

        out[MAP_VISION_HEIGHT // 2][MAP_VISION_WIDTH // 2] = Blocks.player

        return out
