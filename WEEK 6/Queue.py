import numpy as np


class Queue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.array = np.array([None] * self.capacity)
        self.size = 0
        self.front = 0
        self.rear = 0

    def add(self, item):
        if self.size >= self.capacity:
            print("Queue is full. Cannot add more items.")
            return

        self.array[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        print(f"{item} added to the queue.")

    def remove(self):
        if self.size == 0:
            print("Queue is empty. Nothing to remove.")
            return None

        removed_item = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"{removed_item} removed from the queue.")
        return removed_item

    def __str__(self):
        return f"Queue: {self.array[:self.size]} | Size: {self.size} | Capacity: {self.capacity}"


# Example usage
queue = Queue(5)
queue.add('apple')
queue.add('banana')
print(queue)
queue.remove()
print(queue)
queue.add('cherry')
print(queue)
queue.add('date')
queue.add('elderberry')
print(queue)
queue.add('fig')
print(queue)
queue.add('grape')
queue.remove()
queue.remove()
print(queue)
print(queue)
