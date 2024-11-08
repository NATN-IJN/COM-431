from exam_node import Node

class TupleLinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, key, value):
        self.key = key
        self.value = value
        key = input("Please enter a key: ")
        value = input("Please enter a value: ")
        tupl = (key, value)
        new_node = Node(tupl)
        if self.head is None:
            self.head = Node(tupl)
            self.tail = Node(tupl)
            print(f"Succesfully added: {new_node}")
            return
        else:
            self.tail.link(new_node)
            self.tail = new_node
            return


    def find(self):
        searchInput = input("Please enter a key to search: ")
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value[0] == searchInput:
                print(currentNode.value[1])
                return currentNode.value[1]
            else:
                currentNode = currentNode.next
        return None

tll = TupleLinkedLists()
tll.add('cat', 'meow')
tll.find()


