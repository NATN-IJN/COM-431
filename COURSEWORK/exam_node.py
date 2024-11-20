


class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

    def link(self, othernode):
        self.next = othernode
        othernode.prev = self

    def delete(self):
        self.prev = None
        self.next = None
        self.value = None

    # def split(head):
    #     fast = head
    #     slow = head
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next
    #
    #     secondhalf = slow.next
    #     slow.next = None
    #     return secondhalf
    #
    # def merge(first, second):
    #     if not first:
    #         return second
    #     if not second:
    #         return first
    #
    #     if first.data < second.data:
    #         first.next = merge(first,second.next)
    #         return first
    #     else:
    #         second.next = merge(first,second.next)
    #         return second

    # def split(self, head):
    #     self.head = head
    #     fast = head
    #     slow = head
    #     while fast is not None and fast.next is not None and fast.next.next is not None:
    #         fast = fast.next.next
    #         slow = slow.next
    #     temp = slow.next
    #     slow.next = None
    #     if temp is not None:
    #         temp.prev = None
    #     return temp
    #
    # def merge(self, first, second):
    #     self.first = first
    #     self.second = second
    #     if not first:
    #         return second
    #     if not second:
    #         return first
    #
    #     if first.value < second.value:
    #         first.next = merge(first.next, second)
    #         if first.next is not None:
    #             first.next.prev = first
    #         first.prev = None
    #         return first
    #     else:
    #         second.next = merge(first, second.next)
    #         if second.next is not None:
    #             second.next.prev = second
    #         second.prev = None
    #         return second


    def __str__(self):
        return f"Node containing {self.value}"