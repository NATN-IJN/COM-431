class Stack:
    def __init__(self):
        self.internalList = []

    def push(self, item):
        self.internalList.append(item)
        pass

    def pop(self):
        top_item = self.internalList[-1]
        del self.internalList[-1]
        return top_item
        pass

    def peek(self):
        pass

    def __str__(self):
        return self.internalList.__str__()