from node import Node

class LinkedList:
    def __init__(self):

        self.first = None
        self.last = None

    def add(self, new_node):
        if self.first is None:
            self.first = new_node
            self.last = new_node
            return
        else:
            self.last.next = new_node

    def get(self, index):
        pass

    def __str__(self):
        return self.internalList.__str__()
