from tracker import Tracker

class Solver:

    def __init__(self, checker, size: int):
        self.checker = checker
        self.size = size

    def solve(self, data):
        tracker = Tracker()

        final = self.size - 1

        pos = (0, 0)

        while True:
            if (data[pos[0]][pos[1]] == 0):
                pos, data = self.attempt(pos, data, tracker)

            if (pos[0] == final and pos[1] == final):
                break

            if (pos[1] == final):
                pos = (pos[0] + 1, 0)
            else:
                pos = (pos[0], pos[1] + 1)

        return data

    def attempt(self, pos, data, tracker):
        if (self.tryValues(pos, data)):
            tracker.backup(pos, data)
        else:
            try:
                pos, data = tracker.rollback()
            except:
                raise Exception('There is no solution!')
            pos, data = self.attempt(pos, data, tracker)

        return (pos, data)

    def tryValues(self, pos, data):
        for val in range(data[pos[0]][pos[1]] + 1, self.size + 1):
            data[pos[0]][pos[1]] = val
            if self.checker.check(pos, data):
                return True

        return False
