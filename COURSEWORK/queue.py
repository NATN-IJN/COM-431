class Queue:
    def __init__(self):
        self.enquiries = []

    def enqueue(self, query):
        self.enquiries.append(query)
        print(f"Query: *{query}* has been added to the queue.")
        return

    def dequeue(self):
        if len(self.enquiries) == 0:
            return None
        else:
            print(f"Query: *{self.enquiries[0]}* has been removed from the queue.")
            return self.enquiries.pop(0)

    def display(self):

            if len(self.enquiries) == 0:
                print("No enquiries at the moment")
                return
            else:
                for index, query in enumerate(self.enquiries):
                    print(index, query)
                return
            # else:




