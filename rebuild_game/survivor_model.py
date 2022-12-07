from enum import IntEnum
from typing import Optional

from item import Accessory, Armor, Weapon
from pydantic import BaseModel


class SpecificationEnum(IntEnum):
    normal = 0
    medic = 1
    soldier = 2
    farmer = 3
    builder = 4
    scientist = 5

    def __str__(self):
        return f"{self.name}"


class Survivor(BaseModel):
    name: str = "Citizen"
    level: int = 1
    _hp: int = 30
    _attack: int = 3
    _defense: int = 0
    healing_mult: float = 1.0
    farming_mult: float = 1.0
    building_mult: float = 1.0
    research_mult: float = 1.0
    specification: SpecificationEnum = SpecificationEnum.normal
    max_food: int = 30
    curr_food: int = 30
    equipped_weapon: Optional[Weapon]
    equipped_armor: Optional[Armor]
    equipped_accessory: Optional[Accessory]

    def __init__(self, **data):
        super().__init__(**data)
        # TODO use match-casing when moving to Python 3.11
        # Increase attributes given class of survivor
        if self.specification == SpecificationEnum.medic:
            self.healing_mult += 0.5
            self.research_mult += 0.4
        elif self.specification == SpecificationEnum.soldier:
            self._attack += 5
            self._hp += 30
            self._defense += 3
        elif self.specification == SpecificationEnum.farmer:
            self._hp += 10
            self.farming_mult += 0.5
            self.max_food += 20
        elif self.specification == SpecificationEnum.builder:
            self._hp = 20
            self.building_mult += 0.5
            self.max_food += 10
        elif self.specification == SpecificationEnum.scientist:
            self._hp -= 10
            self._attack -= 2
            self.research_mult += 1

    def __str__(self):
        return (
            f"{self.name} [Lv:{self.level}, HP:{self.hp}, Att:{self.attack}, "
            f"Class:{self.specification.name}]"
        )

    @property
    def attack(self) -> int:
        return self._attack + self.equipped_weapon.attack + self.equipped_accessory.attack

    @property
    def hp(self) -> int:
        return self._hp + self.equipped_accessory.hp

    @property
    def defense(self) -> int:
        return self._defense + self.equipped_armor.defense + self.equipped_accessory.attack

    def equip_weapon(self, weapon: Weapon) -> Optional[Weapon]:
        swapped_weapon = self.equipped_weapon
        self.equipped_weapon = weapon
        return swapped_weapon

    def unequip_weapon(self) -> Optional[Weapon]:
        return self.equip_weapon(None)

    def equip_armor(self, armor: Armor) -> Optional[Armor]:
        swapped_armor = self.equipped_armor
        self.equipped_armor = armor
        return swapped_armor

    def unequip_armor(self) -> Optional[Weapon]:
        return self.equip_armor(None)

    def equip_accessory(self, accessory: Accessory) -> Optional[Accessory]:
        swapped_accessory = self.equipped_accessory
        self.equipped_accessory = accessory
        return swapped_accessory

    def unequip_accessory(self) -> Optional[Accessory]:
        return self.equip_accessory(None)
