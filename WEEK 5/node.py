class Node:
      def __init__(self, data):
         self.data = data
         self.prev = None
         self.next = None

      def __str__(self):
         return self.data.__str__()