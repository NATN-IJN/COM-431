class Stack:
    def __init__(self):
        self.internalList = []

    def push(self, item):
        self.internalList.append(item)
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def __str__(self):
        return self.internalList.__str__()