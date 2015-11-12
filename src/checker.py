import math

class Checker:

    def __init__(self, size: int):
        sqrsize = int(math.sqrt(size))

        self.posToSqr = {}
        self.sqrToPos = {}
        self.size = size

        for sqr in range(size):
            self.sqrToPos[sqr] = []

        for row in range(size):
            base = row // sqrsize
            for col in range(size):
                sqr = base * sqrsize + col // sqrsize
                self.posToSqr[(row, col)] = sqr
                self.sqrToPos[sqr].append((row, col))

    def check(self, pos, data):
        value = data[pos[0]][pos[1]]

        if (value == 0):
            return True

        if (value > self.size):
            return False

        if (not self.checkRow(data, pos[0], value)):
            return False

        if (not self.checkCol(data, pos[1], value)):
            return False

        if (not self.checkSqr(data, self.posToSqr[pos], value)):
            return False

        return True

    def checkRow(self, data, row: int, value: int):
        count = 0

        for col in range(self.size):
            if (data[row][col] == value):
                count += 1

        return count < 2

    def checkCol(self, data, col: int, value: int):
        count = 0

        for row in range(self.size):
            if (data[row][col] == value):
                count += 1

        return count < 2

    def checkSqr(self, data, sqr: int, value: int):
        count = 0

        for pos in self.sqrToPos[sqr]:
            if (data[pos[0]][pos[1]] == value):
                count += 1

        return count < 2
