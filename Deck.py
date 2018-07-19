import random
import unittest


class Deck(object):
    class Card(object):
        def __init__(self, name, value, effect):
            self.name = name
            self.value = value
            self.effect = effect

        def __str__(self):
            return str(self.name)

    def __init__(self, file=None):
        self.deck = []
        self.discard = []

        if file:
            my_file = open(file)
            for line in my_file:
                data = line.split(":")
                self.push(data[0], data[1], data[2])
            my_file.close()
            self.shuffle()

    def __contains__(self, item):
        for card in self.deck:
            if card.name == item:
                return True
        return False

    def push(self, name, value, effect):
        self.deck.append(self.Card(name, value, effect))

    def shuffle(self, pile=None):
        shuffled = []
        if not pile:
            pile = self.deck
        while pile:
            shuffled.append(pile.pop(random.randint(0, len(pile)-1)))
        self.deck = shuffled

    def draw(self):
        drawn = self.deck.pop(0)
        self.discard.append(drawn)
        if not self.deck:
            self.shuffle(self.discard)
            self.discard.clear()
        return drawn


class DeckTest(unittest.TestCase):
    def test_build(self):
        test_deck = Deck("test_deck.txt")
        self.assertTrue("card one" in test_deck)
        self.assertFalse("" in test_deck)

    def test_shuffle(self):
        test_deck = Deck("test_deck.txt")
        test_deck.shuffle()
        self.assertTrue("card three" in test_deck)

    def test_draw(self):
        test_deck = Deck("test_deck.txt")
        self.assertEqual(str(test_deck.draw()), "card one")
