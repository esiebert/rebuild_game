from item import Accessory, Armor, Weapon
from survivor_model import Survivor


class Game:
    """docstring for Game"""

    def __init__(self):
        pass

    def run(self):
        survivor = Survivor(
            equipped_weapon=Weapon(
                name="Fist",
                attack=0,
            ),
            equipped_armor=Armor(
                name="Shirt",
                defense=0,
            ),
            equipped_accessory=Accessory(
                name="Ring",
                attack=0,
                hp=0,
                defense=0,
            ),
        )
        print(survivor)


if __name__ == "__main__":
    Game().run()
