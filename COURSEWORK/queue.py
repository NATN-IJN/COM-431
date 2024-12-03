class Queue:
    def __init__(self):
        self.enquiries = []

    def enqueue(self, query):
        self.enquiries.append(query)
        print(f"Query: *{query}* has been added to the queue.")
        return query

    def dequeue(self):
        if len(self.enquiries) == 0:
            return None
        else:
            print(f"Query: *{self.enquiries[0]}* has been removed from the queue.")
            return self.enquiries.pop(0)

    def display(self):
        for index, query in enumerate(self.enquiries):
            print(index, query)
            # else:
            #     print("No enquiries at the moment")



