from DATA.modules.base.print_text import map_print_text

from DATA.modules.variables import *


def debug_window(screen, x: int, y: int, message: str, ):
    pygame.draw.rect(
        screen.screen,
        SCREEN_COLOR, (x, y, len(message) * 12, 20)
    )

    map_print_text(
        screen.screen, x, y, message, (255, 255, 255)
    )
