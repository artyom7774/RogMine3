from DATA.modules.base.print_text import map_print_text
from DATA.modules.base.debug_window import debug_window

from DATA.modules.variables import *
import pygame


class Draw:
    def __init__(self, screen):
        self.screen = screen

    def start(self):
        self.screen.screen.fill(SCREEN_COLOR)

        # create map
        map = []

        for line in range(720 // CELL_SIZE_HEIGHT):
            self.screen.window = self.screen.map.get_screen(self.screen.player.x, self.screen.player.y)

            if line < MAP_VISION_HEIGHT:
                map.append(
                    [[symbol.show, symbol.color] for symbol in self.screen.window[line]] +
                    [[symbol, FRAME_COLOR] for symbol in self.screen.frame_stats.get_line(line)]
                )

            else:
                map.append(
                    [[symbol, FRAME_COLOR] for symbol in self.screen.frame_message.get_line(line - MAP_VISION_HEIGHT)] +
                    [[symbol, FRAME_COLOR] for symbol in self.screen.frame_stats.get_line(line)]
                )

        for i, line in enumerate(map):
            start = 0
            out = line[0][0]

            for j in range(1, 100):
                if line[j][1] == line[j - 1][1]:
                    out += line[j][0]

                else:
                    map_print_text(self.screen.screen, start * CELL_SIZE_WIDTH, i * CELL_SIZE_HEIGHT, str(out), font_color=line[start][1])

                    start = j
                    out = line[j][0]

            map_print_text(self.screen.screen, start * CELL_SIZE_WIDTH, i * CELL_SIZE_HEIGHT, str(out), font_color=line[start][1])

        # action circle
        pygame.draw.circle(
            self.screen.screen, RED,
            (
                MAP_VISION_WIDTH // 2 * CELL_SIZE_WIDTH + CELL_SIZE_WIDTH // 2,
                MAP_VISION_HEIGHT // 2 * CELL_SIZE_HEIGHT + CELL_SIZE_HEIGHT // 2
            ),
            self.screen.player.stats.action_radius, 2
        )

        # debug mode
        if self.screen.debug:
            debug_window(self.screen, 0, 0, f"FPS: {round(self.screen.clock.get_fps(), 1)}")
            debug_window(self.screen, 0, 20, f"X: {self.screen.player.x + 1}")
            debug_window(self.screen, 0, 40, f"Y: {self.screen.player.y + 1}")

        # mouse
        pygame.draw.circle(
            self.screen.screen, RED, 
            (
                self.screen.mouse[0] // CELL_SIZE_WIDTH * CELL_SIZE_WIDTH + CELL_SIZE_WIDTH // 2, 
                self.screen.mouse[1] // CELL_SIZE_HEIGHT * CELL_SIZE_HEIGHT + CELL_SIZE_HEIGHT // 2
            ), 
            8, 2
        )

        pygame.display.update()
