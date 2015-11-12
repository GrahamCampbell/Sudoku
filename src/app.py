from checker import Checker
from reader import Reader
from solver import Solver
from tracker import Tracker

def main(size, path):
    checker = Checker(size)
    reader = Reader(checker, size)
    data = reader.read('data\\' + path)
    solver = Solver(checker, size)

    try:
        return solver.solve(data)
    except Exception as e:
        return str(e)

print(main(4, '4.txt'))
