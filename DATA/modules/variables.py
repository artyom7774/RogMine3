import pygame

pygame.init()

# colors
FRAME_COLOR = (255, 255, 255)
SCREEN_COLOR = (10, 10, 10)
RED = (150, 0, 0)

# project stats
WIDTH = 1200
HEIGHT = 720
FPS = 30

NAME = "RogMine3"
ICONNAME = ""

# map
MAP_WIDTH = 200
MAP_HEIGHT = 200

MAP_VISION_WIDTH = 75
MAP_VISION_HEIGHT = 25

CELL_SIZE_HEIGHT = 20
CELL_SIZE_WIDTH = 12

GENERATE_SPAWN_CHANCE = 5

# player
BASE_PLAYER_SPEED = 7

STAMINA_FOR_RUN = 0.1
STAMINA_FOR_BREAK = 0.2  # STAMINA_FOR_BREAK * player.damage

STAMINA_REGEN = 0.02

INVENTORY_MAX_SIZE = 9

# font
FONT = pygame.font.Font("DATA/files/fonts/lucida.ttf", 20)
