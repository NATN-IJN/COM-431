import sys

class Node:
    def __init__(self, name):
        self.dist = sys.maxsize
        self.name = name
        self.edges = []
        self.isInOpenList = False
        self.removed = False

    def addEdge(self, edge):
        self.edges.append(edge)

    def __lt__(self, other):
        return self.dist < other.dist
