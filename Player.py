import random


class Player(object):

    def __init__(self, num):
        self.num = num
        self.current = None

    @staticmethod
    def roll_dice():
        dice = []
        for roll in range(2):
            dice.append(random.randint(1, 6))
        return dice
