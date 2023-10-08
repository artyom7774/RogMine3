from DATA.modules.inventory import Inventory

from dataclasses import dataclass


class Body:
    out = {
        "head": "HEAD",
        "torso": "TORSO",
        "left_arm": "L.ARM",
        "right_arm": "R.ARM",
        "left_leg": "L.LEG",
        "right_leg": "R.LEG"
    }

    def __init__(self, head, torso, left_arm, right_arm, left_leg, right_leg):
        self.body = {
            "head": head,
            "torso": torso,

            "left_arm": left_arm,
            "right_arm": right_arm,

            "left_leg": left_leg,
            "right_leg": right_leg
        }

    def get(self):
        return list(self.body.values())

    def get_effictivity(self, request):
        var = [self.body[key] for key in self.body.keys() if key in request]
        return sum(var) / len(var)

    def get_name(self, key):
        var = str(round(self.body[key] * 100))
        return f"{self.out[key]}:{' ' * (6 - len(self.out[key]))}{' ' * (3 - len(var)) + var}%"


@dataclass
class Stats:
    go_speed: int
    action_speed: int
    action_radius: int

    damage: int

    stamina_now: int
    stamina_max: int
    stamina_was_using: bool

    body: Body
    inventory: Inventory

    def get(self):
        return [
            self.go_speed,
            self.action_speed,
            self.action_radius,
            self.damage,
            self.stamina_now,
            self.stamina_max,
            self.stamina_was_using,

            self.body.get(),
            self.inventory.get()
        ]
