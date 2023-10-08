from DATA.modules.player import Player
from DATA.modules.map import Map

import json


class Game:
    @classmethod
    def save(cls, screen):
        with open("DATA/files/maps/map.json", "w") as file:
            file.write(json.dumps(screen.map.save()))

        with open("DATA/files/maps/player.json", "w") as file:
            file.write(json.dumps(screen.player.get()))

    @classmethod
    def load(cls, screen):
        try:
            with open("DATA/files/maps/player.json", "r") as file:
                screen.player = Player(screen, *json.load(file))

            with open("DATA/files/maps/map.json", "r") as file:
                screen.map = Map(screen, json.load(file))
                
        except:
            print("ERROR: load")
            
            Game.new(screen)

    @classmethod
    def new(cls, screen):
        screen.player = Player(screen, 0, 0)

        screen.map = Map(screen)
        screen.map.generate()
