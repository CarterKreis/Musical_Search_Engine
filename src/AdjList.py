from Map import *


class AdjList:

    def __init__(self):
        self.graph = Map()

    def insert(self, key, value):
        if key not in self.graph:
            self.graph.insert(key, value=[])

        self.graph.insert(key, value.append(value))

    def search(self, key):
        if key in self.graph:
            return True
        else:
            return False
