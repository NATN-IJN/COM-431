from node import Node

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            return
        else:
            self.last.next = new_node
            self.last = new_node

    def get(self, index):
        current_node = self.first
        current_index = 0

        while current_node is not None:
            if current_index == index:
                return current_node.data
            current_node = current_node.next
            current_index += 1

        raise IndexError("Index out of bounds")

    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.first
            self.first = new_node
            if self.last is None:
                self.last = new_node
            return

        current_node = self.first
        current_index = 0

        while current_node is not None and current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        if current_node is None:
            raise IndexError("Index out of bounds")

        new_node.next = current_node.next
        current_node.next = new_node

        if new_node.next is None:
            self.last = new_node
