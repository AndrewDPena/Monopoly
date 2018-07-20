# file --GameBoard.py--
import GameBoard
import Deck
import CardEffects
import Player
import unittest


class Game:
    def __init__(self, game_file, players=None):
        self.board = GameBoard.GameBoard(game_file)
        self.playerList = []
        self.chance = Deck.Deck("Chance.txt")
        self.community = Deck.Deck("Community_Chest.txt")

        if players:
            for player in range(players):
                self.__add_players(player)

    def __add_players(self, number):
        new = Player.Player(number)
        new.current = 0
        self.playerList.append(new)

    def take_turn(self, player_num):
        player = self.playerList[player_num-1]
        roll_total = 0
        roll = player.roll_dice()
        if roll[0] == roll[1]:
            player.double_count += 1
        else:
            player.double_count = 0
        if player.double_count == 3:
            player.current = 10
        else:
            for number in roll:
                roll_total += number
            # current_index = self.board.tiles.index(player.current)
            player.current = (player.current + roll_total) % len(self.board.tiles)
            self.check_position(player)
            if player.double_count > 0:
                self.take_turn(player_num)

    def check_position(self, player):
        self.board.tiles[player.current].count += 1
        if self.board.tiles[player.current].name == "Go To Jail":
            player.current = 10
        elif self.board.tiles[player.current].color == "Chnc" or self.board.tiles[player.current].color == "Comm":
            self.draw_card(player)

    def draw_card(self, player):
        if self.board.tiles[player.current].color == "Chnc":
            drawn = self.chance.draw()
        else:
            drawn = self.community.draw()
        if drawn.value == "12" and player.current > int(drawn.value):  # utility card
            drawn.value = 28
        if drawn.value == "5":  # railroad card
            next_rail = int(player.current)
            next_rail += 10 - ((player.current + 5) % 10)
            next_rail %= len(self.board.tiles)
            drawn.value = str(next_rail)
        getattr(CardEffects.CardEffects(), drawn.effect)(player, drawn.value)
        if drawn.effect == "move_player":
            self.check_position(player)


if '__main__' == __name__:
    monopolyGame = Game("Monopoly.txt", 1)
    for _ in range(5000000):
        monopolyGame.take_turn(1)
    # monopolyGame.board.print_count()
    monopolyGame.board.save_count()
    # unittest.main(GameBoard)


class TestGoToJail(unittest.TestCase):
    def test(self):
        test_game = Game("Monopoly.txt", 1)
        test_player = test_game.playerList[0]
        test_player.current = 30
        self.assertEqual(test_game.board.tiles[test_player.current].name, "Go To Jail")
        test_game.check_position(test_player)
        self.assertEqual(test_game.board.tiles[test_player.current].name, "Jail")

    def test_deck(self):
        test_game = Game("Monopoly.txt", 1)
        self.assertTrue("Advance to GO" in test_game.chance)

    def test_position(self):
        test_game = Game("Monopoly.txt", 1)
        test_player = test_game.playerList[0]
        test_player.current = 7
        self.assertEqual(test_game.board.tiles[test_player.current].color, "Chnc")

    def test_card(self):
        test_game = Game("Monopoly.txt", 1)
        test_player = test_game.playerList[0]
        test_player.current = 7
        test_game.chance = Deck.Deck()
        test_game.chance.push("Go to Jail", "10", "move_player")
        test_game.draw_card(test_player)
        self.assertEqual(test_game.playerList[0].current, 10)

    def test_railroad(self):
        test_game = Game("Monopoly.txt", 1)
        test_player = test_game.playerList[0]
        test_player.current = 22
        test_game.chance = Deck.Deck()
        test_game.chance.push("Go to nearest Railroad", "5", "move_player")
        test_game.draw_card(test_player)
        self.assertEqual(test_game.playerList[0].current, 25)

    def test_speeding(self):
        test_game = Game("Monopoly.txt", 1)
        test_game.chance = Deck.Deck()
        test_game.community = test_game.chance
        test_game.chance.push("Test Card", "0", "pay_player")
        test_player = test_game.playerList[0]
        test_player.debug = True
        test_player.double_count = 2
        test_game.take_turn(1)
        self.assertEqual(test_player.current, 10)
