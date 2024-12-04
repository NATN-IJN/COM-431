#Imorts all relevant classes
from queue import Queue
from node import Node
from merge_sort import MS
import random

class TuplesLinkedList:
#Initializes head and tail of Linked List to None
    def __init__(self):
        self.first = None
        self.last = None

#Adds newly created nodes to create "TuplesLinkedList"
    def add(self, name, value, description, uid):
        key_value = (name, value, description, uid)
        n = Node(key_value)
        if self.first is None:
            self.first = n
            self.last = n
            print(f"Successfully added first: {n}")
        else:
            self.last.link(n)
            self.last = n
            print(f"Successfully added {n}")

#Using ID generated from randint function, this method iterates through list to find index with match
    def findid(self, uid):
        currentNode = self.first
        while currentNode is not None:
            if currentNode.value[3] == uid:
                print(f"Age Rating: {currentNode.value[1]}, Genre: {currentNode.value[2]}")
                return
            else:
                currentNode = currentNode.next
        return

#Using ID , method iterates through linked list to find matching value. It then calls delete method from Node class
    def dlt(self, uid):
        currentnode = self.first
        while currentnode is not None:
            if currentnode.value[3] == uid:
                print(f"  Movie:  {currentnode.value[0]}  |  Age Rating: {currentnode.value[1]}  |  Genre: {currentnode.value[2]} -  will be deleted...")
                currentnode.delete()
                return
            else:
                currentnode = currentnode.next
        return None

#Using ID it locates node to save
    def sve(self, uid):
        currentnode = self.first
        while currentnode is not None:
            if currentnode.value[3] == uid:
                name = currentnode.value[0]
                age = currentnode.value[1]
                genre = currentnode.value[2]


                tupl = [f"  NAME: {(name)}  |  AGE: {(age)}  |  GENRE: {(genre)}  "]
                with open('movie.txt', "a") as f:
                        f.write(f'{tupl}\n')
                print(f"{tupl} will be saved")
                break
        print("Movie not found:")

        ans = 0
        while ans != "y" and ans != "n":
            ans = input("Would you like to view saved Movies? (y/n): ").lower()
            if ans == 'y':
                with open('movie.txt', 'r') as f:
                   content = f.read()
                print(content)

            elif ans == 'n':
                return None

            else:
                print("Please enter y or n")

#Finds matching node using key provided by user and then returns the ID number
    def return_id(self, key):
        currentnode = self.first
        while currentnode is not None:
            if currentnode.value[0] == key:
                return currentnode.value[3]
            else:
                currentnode = currentnode.next

class HashTable:
    def __init__(self,size=127):
        self.first = None
        self.size = size
        self.buckets = [TuplesLinkedList() for i in range(self.size)]


#Unique formula for calculating hash code, iterates through each character in key (ID number)
# and finds ASCII value using "ord"
    def hash(self,key):
        hash_code = 0
        index = 0
        for items in key:
            hash_code+=ord(items)*(31**(index))
            index+=1
        return hash_code

#Asks users to input movie details, then passes through the add function.
    def put(self):
        name = input("Please enter Movie Name: ")
        rating = input("Please Movie Age Rating: ")
        genre = input("Please enter Movie Genre: ")
        uid = random.randint(0,self.size)
        uidstr = str(uid)
        hash_code = self.hash(uidstr)
        print(f"Your unique ID number is: {hash_code}")
        bucket_index = (hash_code%127)
        self.buckets[bucket_index].add(name, rating, genre, hash_code)
        return
#Enables user a choice of how to search. It then calls findid/return_id function depending on option
    def search(self):
        print("""
        Please enter a number:
        1. Search by Movie Name
        2. Search by ID
        NOTE *** Please search by ID if there are other movies with the same movie name ***""")
        try:
            ans = input()
            if ans == '1':
                key = input("Please enter movie name: ")
                for bucket in self.buckets:
                    userid = bucket.return_id(key)
                    if userid is not None:
                        bucket.findid(userid)
                        return

            elif ans == '2':
                uid = int(input("Please enter the ID number: "))
                bucket_index = (uid % 127)
                return self.buckets[bucket_index].findid(uid)

            else:
                print("Invalid input! please enter 1 or 2")
        except Exception as e:
            print("movie does not exist", e)

#Calls dlt method from "Tupleslinkedlist"
    def delete(self):
        uid = int(input("Please enter movie ID : "))
        bucket_index = (uid % 127)
        self.buckets[bucket_index].dlt(uid)

#calls save method from  "TuplesLinkedList"
    def save(self):
        print("Please enter movie ID: ")
        try:
            ans = int(input())
            bucket_index = (ans % 127)
            if self.buckets[bucket_index] is not None:
                self.buckets[bucket_index].sve(ans)
                return
        except Exception as e:
            print("Movie not found", e)

    def dply(self):
            print("Displaying all saved movies:")

            # Collect all entries from all buckets
            all_nodes = []
            for bucket in self.buckets:
                current = bucket.first
                while current:
                    all_nodes.append(current.value)  # Collect values from linked list
                    current = current.next

            if not all_nodes:
                print("No movies found.")
                return

            # Sort the aggregated list using MS
            ms = MS(None)  # Pass None because we're sorting a list, not a linked list
            sorted_nodes = ms.merge_sort(all_nodes)

            # Display sorted results
            for node in sorted_nodes:
                print(f"Name: {node[0]}, Age Rating: {node[1]}, Genre: {node[2]}, UID: {node[3]}")

#Calls "Hashtable" class
enq = Queue()
ht = HashTable()
ht.hash('')


#Loops menu until "6" key is entered
while True:
        print("""Please enter a number
          1. Add Movie: 
          2. Search Movie: 
          3. Delete Movie: 
          4. Save Movie: 
          5. Display Movies: 
          6. Exit: 
          ---------------
          8. Enquiries: """)
        try:
            menu = int(input())
            if menu == 1:
                ht.put()
            elif menu == 2:
                 ht.search()
            elif menu == 3:
                ht.delete()
            elif menu == 4:
                ht.save()
            elif menu == 5:
                ht.dply()
            elif menu == 6:
                print("Application terminated")
                break


            elif menu == 8:
                print(""" 
                Please enter a number:
                1. Add query:
                2. Answer query:
                3. Show query's:""")
                ans = input()
                if ans == '1':
                    query = input("Enter your query: ")
                    enq.enqueue(query)
                    enq.display()
                if ans == '2':
                    enq.dequeue()
                if ans == '3':
                    enq.display()
                else:
                    print("Invalid Input")
            else:
                print("Invalid input!, please enter a number between 1 and 6")
        except ValueError:
            print("Invalid input!, please enter a number")
