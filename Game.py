#file --GameBoard.py--
import GameBoard, Player, unittest

if '__main__' == __name__:
    my_board = GameBoard.gameboard("testfile.txt")
    my_board.print_board()
    #unittest.main(GameBoard)