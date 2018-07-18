# file --GameBoard.py--
import GameBoard
import Player
import unittest


class Game:
    def __init__(self, game_file, players=None):
        self.board = GameBoard.GameBoard(game_file)
        self.playerList = []

        if players:
            for player in range(players):
                self.__add_players(player)

    def __add_players(self, number):
        new = Player.Player(number)
        new.current = self.board.start
        self.playerList.append(new)

    def take_turn(self, player_num):
        player = self.playerList[player_num-1]
        roll_total = 0
        roll = player.roll_dice()
        for number in roll:
            roll_total += number
        current_index = self.board.tiles.index(player.current)
        player.current = self.board.tiles[(current_index + roll_total) % len(self.board.tiles)]
        player.current.count += 1

        self.check_position(player)

    def check_position(self, player):
        if player.current.name == "Go To Jail":
            player.current = self.board.tiles[10]


if '__main__' == __name__:
    monopolyGame = Game("testfile.txt", 1)
    for _ in range(5000000):
        monopolyGame.take_turn(1)
    # monopolyGame.board.print_count()
    monopolyGame.board.save_count()
    # unittest.main(GameBoard)


class TestGoToJail(unittest.TestCase):
    def test(self):
        test_game = Game("testfile.txt", 1)
        test_player = test_game.playerList[0]
        test_player.current = test_game.board.tiles[30]
        self.assertEqual(test_player.current.name, "Go To Jail")
        test_game.check_position(test_player)
        self.assertEqual(test_player.current.name, "Jail")
