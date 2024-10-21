class Stack:
      def __init__(self):
         self.internalList = []

      def push(self, item):
          self.internalList.append(item)

      def pop(self):
          if len(self.internalList) == 0:
             raise Exception("Stack is empty")
             return None
          else:
              top_item = self.internalList[-1]
              del self.internalList[-1]
              return top_item


      def __str__(self):
          return self.internalList.__str__()