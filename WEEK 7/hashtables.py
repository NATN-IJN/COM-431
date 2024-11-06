from ht_node import Node


class TuplesLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    # TODO modify "add()" so that it takes a key and a value as parameters and
    # creates a  tuple using them. The Node should then be created using the
    # tuple.
    def add(self, key, value):
        key_value = (key, value)
        n = Node(key_value)
        if self.first is None:
            self.first = n
            self.last = n
        else:
            self.last.link(n)
            self.last = n

    def get(self, index):
        counter = 0
        currentNode = self.first
        while currentNode is not None:
            if counter == index:
                return currentNode
            else:
                currentNode = currentNode.next
                counter += 1
        return None

    # TODO modify "find()" so that it takes a KEY as a parameter  and searches
    # the linked list until it finds a tuple with that key. It should then
    # return the value (i.e. the second member of the tuple)
    def find(self, searchInput):
        currentNode = self.first
        while currentNode is not None:
            if currentNode.value[0] == searchInput:
                return currentNode.value[1]
            else:
                currentNode = currentNode.next
        return None

class HashTable:
    def __init__(self,size=127):
        self.size = size
        self.buckets = [TuplesLinkedList() for _ in range(self.size)]

    def hash(self,key):
        code = 0
        index = 0
        for items in key:
            code+=ord(items)*(31**(index))
            index+=1
        return code

    def put(self,key,value):
        code = self.hash(key)
        bucket_index = code%127
        self.buckets[bucket_index].add(key, value)

    def search(self,key):
        code = self.hash(key)
        bucket_index = code % 127
        return self.buckets[bucket_index].find(key)












ht = HashTable()
ht.hash('act',1)









