import unittest

class gameboard(object):
    class boardtile(object):
        def __init__(self, name, color, value, next):
            self.name = name
            self.color = color
            self.value = value
            self.next = next
            self.count = 0

        def __str__(self):
            return self.name + " : " + self.color + " : " + self.value

    def __init__(self, file=None):
        self.front = self.back = self.current = None

        if file:
            my_file = open(file)
            for line in my_file:
                data = line.split(":")
                #print(data[0])
                self.push(data[0], data[1], data[2])
                #print(data[1])

    def empty(self):
        return self.front == self.back == None

    def __iter__(self):
        self.current = self.front
        return self

    def __next__(self):
        if self.current:
            tmp = self.current.value
            self.current = self.current.next_node
            return tmp
        else:
            raise StopIteration()

    def push(self, name, color, value):
        new = self.boardtile(name, color, value, self.front)
        if self.empty():
            self.back = self.front = new
        else:
            self.back.next = new
            self.back = new

    def print_board(self):
        tmp = self.front
        if self.empty():
            raise RuntimeError
        print(tmp)
        tmp = tmp.next
        while tmp != self.front:
            print(tmp)
            tmp = tmp.next

    def landing_totals(self):
        tmp = self.front
        if self.empty():
            raise RuntimeError
        print(tmp.name + " : " + tmp.count)
        tmp = tmp.next
        while tmp != self.front:
            print(tmp.name + " : " + tmp.count)
            tmp = tmp.next


class TestPush(unittest.TestCase):
    def test_empty(self):
        test_board = gameboard()
        self.assertTrue(test_board.empty())

    def test_pushes(self):
        test_board = gameboard()
        test_board.push("one", "red", 6)
        test_board.push("two", "blue", 2)
        self.assertEqual(test_board.front.name, "one")
        self.assertEqual(test_board.front.color, "red")
        self.assertEqual(test_board.front.next.name, "two")
        self.assertEqual(test_board.front.next.next.name, "one")
