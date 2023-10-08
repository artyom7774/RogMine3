from DATA.modules.variables import *


class Inventory:
    """
    item = {
        name: str,
        count: int
    }
    """

    def __init__(self, inventory: list = []):
        self.inventory = inventory

    def add(self, add_item: dict):
        for i, item in enumerate(self.inventory):
            if add_item["name"] == item["name"]:
                self.inventory[i]["count"] += add_item["count"]

        else:
            if len(self.inventory) < INVENTORY_MAX_SIZE: 
                self.inventory.append(add_item)

            else:
                raise NameError(f"len inventory bigger than {INVENTORY_MAX_SIZE}")

    def remove(self, remove_item: dict):
        for i, item in enumerate(self.inventory):
            if remove_item["name"] == item["name"]:
                if remove_item["count"] <= item["count"]:
                    self.inventory[i]["count"] -= remove_item["count"]

                    if self.inventory[i]["count"] == 0:
                        self.inventory.pop(i)

                    break

                else:
                    raise NameError("count remove item not in inventory")

            else:
                raise NameError("remove item not fined in inventory")

    def have(self, have_item: dict):
        for i, item in enumerate(self.inventory):
            if have_item["name"] == item["name"]:
                if have_item["count"] <= item["count"]:
                    return True
                    
                else:
                    return False

        return False

    def get(self):
        return self.inventory
