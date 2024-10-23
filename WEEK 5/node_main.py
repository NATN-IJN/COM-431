from linkedlist import LinkedList

from linkedlist import LinkedList

linked_list = LinkedList()


linked_list.add(1)
linked_list.add(2)
linked_list.add(3)


try:
    print(linked_list.get(0))
    print(linked_list.get(1))
    print(linked_list.get(2))
    print(linked_list.get(10))
except IndexError as e:
    print(e)

linked_list.insert(1, 1.5)
print(linked_list.get(1))

