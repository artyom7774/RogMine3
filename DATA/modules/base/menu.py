from DATA.modules.entity import Blocks

from DATA.modules.variables import *


class Menu:
    @classmethod
    def frame_stats(cls, screen):
        stamina = round(round(screen.player.stats.stamina_now / screen.player.stats.stamina_max, 1) * 10)

        if screen.mouse[1] // CELL_SIZE_HEIGHT < MAP_VISION_HEIGHT and screen.mouse[0] // CELL_SIZE_WIDTH < MAP_VISION_WIDTH:
            item = screen.window[screen.mouse[1] // 20][screen.mouse[0] // 12]
        else:
            item = Blocks.air

        return [
            f"STAMINA: |{'█' * stamina}{'▒' * (10 - stamina)}|",
            f"&empty&",
            f"{screen.player.stats.body.get_name('head')}",
            f"{screen.player.stats.body.get_name('torso')}",
            f"{screen.player.stats.body.get_name('left_arm')}",
            f"{screen.player.stats.body.get_name('right_arm')}",
            f"{screen.player.stats.body.get_name('left_leg')}",
            f"{screen.player.stats.body.get_name('right_leg')}",
            f"&line&",
            f"name: {item.name} ({item.show})",
            f"health: {item.health}",
            f"",
            f"",
            f"",
            f"",
            f"",
            f"",
            f"&line&",
            f"speed: {round(screen.player.stats.go_speed, 1)}",
            f"&empty&",
            f"action speed: {round(screen.player.stats.action_speed, 1)}",
            f"action radius: {round(screen.player.stats.action_radius, 1)}",
            f"22",
            f"23",
            f"24",
            f"25",
            f"26",
            f"27",
            f"28",
            f"29",
            f"30",
            f"31",
            f"32",
            f"33",
            f"34"
        ]

    @classmethod
    def frame_message(cls, screen):
        return [
            f"1", 
            f"2", 
            f"3", 
            f"4", 
            f"5", 
            f"6", 
            f"7", 
            f"8", 
            f"9"
        ]
