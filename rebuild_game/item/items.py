from pydantic import BaseModel


class Item(BaseModel):
    name: str


class Weapon(Item):
    attack: int


class Armor(Item):
    defense: int


class Accessory(Item):
    attack: int
    defense: int
    hp: int
