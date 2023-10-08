from DATA.modules.variables import *
from dataclasses import dataclass


@dataclass
class Block:
    program_name: str
    health: int
    request: list
    passability: bool
    color: tuple
    name: str
    show: str
    id: str

    def get(self):
        return [
            self.program_name,
            self.health,
            self.request,
            self.passability,
            self.color,
            self.name,
            self.show,
            self.id
        ]


@dataclass
class Item:
    program_name: str
    passability: bool
    color: tuple
    name: str
    show: str
    id: str

    def get(self):
        return [
            self.program_name,
            self.passability,
            self.color,
            self.name,
            self.show,
            self.id
        ]


@dataclass
class Entity:
    program_name: str
    health: int
    color: tuple
    name: str
    show: str
    id: list


class Blocks:
    """
    g - game
    r - resource
    e - entity
    s - spawn
    i - item
    n - null

    """

    air = Block("air", -1, [], True, (255, 255, 255), "air", ".", "g-0-0")
    border = Block("border", -1, [], False, (255, 255, 255), "border", "#", "g-0-1")
    null = Block("", "", [], True, (0, 0, 0), "", "", "n-0")

    tree = Block("tree", 20, ["left_arm", "right_arm"], False, (0, 130, 0), "tree", "T", "rs-1-0")
    stone = Block("stone", 35, ["left_arm", "right_arm"], False, (180, 180, 180), "stone", "S", "rs-1-1")

    item_tree = Item("item_tree", True, (0, 130, 0), "tree", "t", "ri-2-0")
    item_stone = Item("item_stone", True, (180, 180, 180), "stone", "s", "ri-2-1")

    player = Entity("player", -1, RED, "player", "@", "e-3-0")
