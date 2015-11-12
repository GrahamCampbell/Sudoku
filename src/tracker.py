import copy

class Tracker:

    def __init__(self):
        self.states = []

    def backup(self, pos, data):
        self.states.append((pos, copy.deepcopy(data)))

    def rollback(self):
        return self.states.pop()
