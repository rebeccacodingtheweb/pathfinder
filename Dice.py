from random import randint


class Dice:
    def __init__(self, face):
        self.face = face

    def roll_dice(self):
        return randint(1, self.face)




