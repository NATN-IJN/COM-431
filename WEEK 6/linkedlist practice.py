class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        itr = self.head
        llstr = ''
        while itr is not None:
            llstr += str(itr.data) + '-->'
            itr = itr.next
            if itr is None:
                break
if __name__ == '__main__':
    ll=LinkedList()
    ll.print_list()