import random


class Player(object):

    def __init__(self, num):
        self.debug = False
        self.num = num
        self.current = None
        self.account = 1000
        self.inventory = set()
        self.double_count = 0

    def roll_dice(self):
        if self.debug:
            return [1, 1]
        dice = []
        for roll in range(2):
            dice.append(random.randint(1, 6))
        return dice
