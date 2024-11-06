import numpy as np

class PriorityQueue:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.array = np.array([None] * self.capacity)
        self.front = 0
        self.rear = 0
        self.size = 0

    def add (self, item, priority):
        if self.size >= self.capacity:
            print("Queue is full")
            return

        self.array[self.rear] = item
        self.array[self.front] = priority
        self.front = (self.front + 1) % self.capacity
        self.size += 1

    def __str__(self):
        return f"Queue: {self.array[:self.size]}  | Size: {self.size}  | Capacity: {self.capacity}  | Priority: {self.array[self.front]}"

pq = PriorityQueue()
pq.add("apple", 1)
pq.add("orange", 2)
pq.add("pear", 3)
print(pq)