from DATA.modules.inventory import Inventory
from DATA.modules.stats import Stats, Body

from DATA.modules.variables import *

BASE_PLAYER_STATS = Stats(7, 3.5, 80, 5, 10, 10, False, Body(1.0, 1.0, 1.0, 1.0, 1.0, 1.0), Inventory([]))


class Player:
    routes = {
        "right": (1, 0),
        "left": (-1, 0),
        "up": (0, -1),
        "down": (0, 1)
    }

    def __init__(self, screen, x: int, y: int, stats: Stats = BASE_PLAYER_STATS):

        self.screen = screen

        self.stats = Stats(*stats[:-2], Body(*stats[-2]), Inventory(stats[-1])) if isinstance(stats, list) else stats
        self.run = False

        self.cd = 0

        self.x = x
        self.y = y

    def get(self):
        return [
            self.x,
            self.y,
            self.stats.get()
        ]

    def update(self):
        self.cd -= 1

        self.stats.go_speed = BASE_PLAYER_SPEED * self.stats.body.get_effictivity(["left_leg", "right_leg"])

        if self.run:
            self.stats.go_speed *= 1.5

        else:
            self.stats.stamina_now = min(self.stats.stamina_now + STAMINA_REGEN, self.stats.stamina_max)

            if self.stats.stamina_now * 2.1 >= self.stats.stamina_max:
                self.stats.stamina_was_using = False

    def move(self, route: str):
        dx, dy = self.routes[route]

        if self.cd <= 0 < self.stats.go_speed:
            if 0 <= self.x + dx < MAP_WIDTH and 0 <= self.y + dy < MAP_HEIGHT:
                if self.screen.map.map[self.y + dy][self.x + dx].passability:
                    self.x += dx
                    self.y += dy

                    self.cd = FPS / self.stats.go_speed

                    if self.run:
                        self.stats.stamina_now -= STAMINA_FOR_RUN
