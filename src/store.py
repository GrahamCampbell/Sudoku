import copy

class Store:

    def __init__(self):
        self.items = []

    def add(self, data):
        self.items.append(copy.deepcopy(data))

    def all(self):
        return copy.deepcopy(self.items)
