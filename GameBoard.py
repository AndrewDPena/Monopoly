import unittest


class GameBoard(object):
    class BoardTile(object):
        def __init__(self, name, color, value):
            self.name = name
            self.color = color
            self.value = value
            self.count = 0

        def __str__(self):
            return self.name + " : " + self.color + " : " + self.value

    def __init__(self, file=None):
        self.start = None
        self.tiles = []

        if file:
            my_file = open(file)
            for line in my_file:
                data = line.split(":")
                self.push(data[0], data[1], data[2])
            my_file.close()
            self.start = self.tiles[0]

    def empty(self):
        return len(self.tiles) == 0

    def __iter__(self):
        return iter(self.tiles)

    def __str__(self):
        result = ""
        for tile in self:
            result += tile.name + '\n'
        return result

    def push(self, name, color, value):
        new = self.BoardTile(name, color, value)
        self.tiles.append(new)

    @staticmethod
    def merge(first, second):
        result = []
        while first or second:
            if not first:
                result.append(second.pop(0))
            elif not second:
                result.append(first.pop(0))
            elif first[0].count < second[0].count:
                result.append(first.pop(0))
            else:
                result.append(second.pop(0))
        return result

    def sort(self, unsorted=None):
        if unsorted is None:
            unsorted = self.tiles
        if not unsorted:
            return unsorted
        if len(unsorted) == 1:
            return unsorted
        midpoint = len(unsorted) // 2
        return self.merge(self.sort(unsorted[:midpoint]), self.sort(unsorted[midpoint:]))

    def print_board(self):
        for tile in self:
            print(tile)

    def print_count(self):
        for tile in self.sort():
            print(tile.name + " : " + str(tile.count))

    def save_count(self):
        output = open("output.txt", "w+")
        for tile in self.sort():
            output.write(tile.name + " : " + str(tile.count) + '\n')
        output.close()


class TestFunctions(unittest.TestCase):
    def test_empty(self):
        test_board = GameBoard()
        self.assertTrue(test_board.empty())

    def test_pushes(self):
        test_board = GameBoard()
        test_board.push("one", "red", 6)
        test_board.push("two", "blue", 2)
        self.assertEqual(test_board.tiles[0].name, "one")
        self.assertEqual(test_board.tiles[0].color, "red")
        self.assertEqual(test_board.tiles[1].name, "two")

    def test_build(self):
        test_board = GameBoard("testfile.txt")
        self.assertEqual(test_board.start.name, "Go")
        self.assertEqual(test_board.tiles[1].name, "Mediterranean Avenue")
        self.assertEqual(test_board.tiles[-1].name, "Boardwalk")

    def test_count_sort(self):
        test_board = GameBoard()
        test_board.push("one", "blue", 0)
        test_board.push("two", "blue", 0)
        test_board.push("three", "blue", 0)
        test_board.push("four", "blue", 0)
        test_board.tiles[0].count += 5
        test_board.tiles[1].count += 2
        test_board.tiles[2].count += 6
        test_board.tiles[3].count += 1
        sorted_list = [test_board.tiles[3], test_board.tiles[1], test_board.tiles[0], test_board.tiles[2]]
        self.assertEqual(test_board.sort(), sorted_list)

    def test_print(self):
        test_board = GameBoard()
        test_board.push("one", "blue", 0)
        test_board.push("two", "blue", 0)
        test_board.push("three", "blue", 0)
        self.assertEqual(str(test_board), "one\ntwo\nthree\n")
