
from random import randint


class die:
    def __init__(self, sides = 6) -> None:
        if sides>=1:
            self.sides = sides
        else: 
            self.sides = 6

    def roll(self) -> int:
        return randint(1, self.sides)

    def __repr__(self) -> str:
        return "You're a bitch\n"
