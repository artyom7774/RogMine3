from DATA.modules.variables import *


def map_print_text(screen, x, y, message, font_color=(255, 255, 255), font_size=20):
    text = FONT.render(message, True, font_color)
    screen.blit(text, (x, y))


def print_text(screen, x, y, message, font_size, font_color=(0, 0, 0), font_type="DATA/files/fonts/lucida.ttf"):
    font = pygame.font.Font(font_type, font_size)
    text = font.render(message, True, font_color)
    screen.blit(text, (x, y))

