import numpy as np


class Queue:
    def __init__(self, capacity=5):
        """Initialize the queue with a specified capacity, default is 5."""
        self.capacity = capacity
        self.array = np.array([None] * self.capacity)  # Internal array initialized to None
        self.size = 0  # Number of elements currently in the queue
        self.front = 0  # Index of the front of the queue
        self.rear = 0  # Index of the rear of the queue

    def add(self, item):
        """Add an item to the rear of the queue."""
        if self.size >= self.capacity:
            print("Queue is full. Cannot add more items.")
            return

        self.array[self.rear] = item  # Add item at the rear position
        self.rear = (self.rear + 1) % self.capacity  # Update rear index circularly
        self.size += 1  # Increase the size of the queue
        print(f"{item} added to the queue.")

    def remove(self):
        """Remove and return an item from the front of the queue."""
        if self.size == 0:
            print("Queue is empty. Nothing to remove.")
            return None

        removed_item = self.array[self.front]  # Get the item to remove
        self.array[self.front] = None  # Clear the position
        self.front = (self.front + 1) % self.capacity  # Update front index circularly
        self.size -= 1  # Decrease the size
        print(f"{removed_item} removed from the queue.")
        return removed_item

    def __str__(self):
        """Return a string representation of the queue's internal state."""
        return f"Queue: {self.array[:self.size]} | Size: {self.size} | Capacity: {self.capacity}"


# Example usage
queue = Queue(5)  # Create a queue with a capacity of 5
queue.add('apple')
queue.add('banana')
print(queue)  # Show the current state of the queue
queue.remove()
print(queue)  # Show the state after removing an item
queue.add('cherry')
print(queue)  # Show the current state of the queue