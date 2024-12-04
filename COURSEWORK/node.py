
class Node:
#Initialises node
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

#links current node(self) with the next node in the Linked list
    def link(self, othernode):
        self.next = othernode
        othernode.prev = self

#Evaluates Node value to "None", deleting it.
    def delete(self):
        self.prev = None
        self.next = None
        self.value = None




    def __str__(self):
        return f"movie containing: {self.value}