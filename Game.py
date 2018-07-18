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

    def take_turn(self, player):
        roll_total = 0
        roll = player.roll_dice()
        for number in roll:
            roll_total += number
        current_index = self.board.tiles.index(player.current)
        player.current = self.board.tiles[(current_index + roll_total) % len(self.board.tiles)]
        player.current.count += 1


if '__main__' == __name__:
    # monopolyGame = Game("testfile.txt", 1)
    unittest.main(GameBoard)
