from exam_node import Node

import random
class TuplesLinkedList:
    def __init__(self):
        self.first = None
        self.last = None


    def add(self, key, value, description, uid):
        key_value = (key, value, description, uid)
        n = Node(key_value)
        if self.first is None:
            self.first = n
            self.last = n
            print(f"Successfully added first: {n}")
        else:
            self.last.link(n)
            self.last = n
            print(f"Successfully added: {n}")


    def get(self, index):
        counter = 0
        currentNode = self.first
        while currentNode is not None:
            if counter == index:
                return currentNode
            else:
                currentNode = currentNode.next
                counter += 1
        return None


    def findid(self, id):
        currentNode = self.first
        while currentNode is not None:
            if currentNode.value[3] == id:
                print(f"Age Rating: {currentNode.value[1]}, Genre: {currentNode.value[2]}")
                return
            else:
                currentNode = currentNode.next
        return

    def findname(self, id):
        currentNode = self.first
        while currentNode is not None:
            if currentNode.value[3] == id:
                print(f"Age Rating: {currentNode.value[1]}, Genre: {currentNode.value[2]}")
                return
            else:
                currentNode = currentNode.next

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

    def sve(self, uid):
        currentnode = self.first
        while currentnode is not None:
            if currentnode.value[3] == uid:
                name = currentnode.value[0]
                age = currentnode.value[1]
                genre = currentnode.value[2]


                tupl = [f"  NAME: {(name)}  |  AGE: {(age)}  |  GENRE: {(genre)}  "]
                with open('poi.txt', "a") as f:
                        f.write(f'{tupl}\n')
                print(f"{tupl} will be saved")
                break

        ans = 0
        while ans != "y" and ans != "n":
            ans = input("Would you like to view saved Movies? (y/n): ").lower()
            if ans == 'y':
                with open('poi.txt', 'r') as f:
                   content = f.read()
                print(content)

            elif ans == 'n':
                return None

            else:
                print("Please enter y or n")

    def display(self):
        currentnode = self.first
        newdict = {}
        if currentnode is not None:
            while currentnode is not None:
                newdict.update({currentnode.value[0]: [currentnode.value[1], currentnode.value[2], currentnode.value[3]]})
                sdict1 = dict(sorted(newdict.items()))
                print(sdict1)
                return currentnode.value[0], currentnode.value[1], currentnode.value[2]
        else:
            return None

    def return_id(self, key):
        currentnode = self.first
        while currentnode is not None:
            if currentnode.value[0] == key:
                return currentnode.value[3]
            else:
                currentnode = currentnode.next

    def extract_and_sort(self):
        nodes = []
        currentnode = self.first

        # Extract all nodes as a list of tuples
        if currentnode is not None:
            while currentnode is not None:
                nodes.append(currentnode.value)  # Add the tuple (key, value, description, uid)
                currentnode = currentnode.next


            # Perform merge sort on the nodes based on the key (alphabetically)
            sorted_nodes = self.merge_sort(nodes)

            # Display the sorted results
            for node in sorted_nodes:
                if node is not None:
                    print(f"Name: {node[0]}, Age Rating: {node[1]}, Genre: {node[2]}, UID: {node[3]}")
                else:
                    pass

    def merge_sort(self, nodes):
        if len(nodes) <= 1:
            return nodes
        else:
            mid = len(nodes) // 2
            left_half = self.merge_sort(nodes[:mid])
            right_half = self.merge_sort(nodes[mid:])

            return self.merge(left_half, right_half)

    def merge(self, left, right):
        sorted_list = []
        i = j = 0

        # Merge two sorted halves
        while i < len(left) and j < len(right):
            if left[i][0].lower() <= right[j][0].lower():  # Compare key (case-insensitive)
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        # Append remaining elements
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])

        return sorted_list




class HashTable:
    def __init__(self,size=127):
        self.first = None
        self.size = size
        self.buckets = [TuplesLinkedList() for i in range(self.size)]

    def hash(self,key):
        hash_code = 0
        index = 0
        for items in key:
            hash_code+=ord(items)*(31**(index))
            index+=1
        return hash_code

    def put(self, name, rating, genre, uid):
        self.name = name
        self.rating = rating
        self.genre = genre
        self.uid = uid
        name = input("Please enter Movie Name")
        rating = input("Please Movie Age Rating")
        genre = input("Please enter Movie Genre")
        uid = random.randint(0,self.size)
        uidstr = str(uid)
        hash_code = self.hash(uidstr)
        print(f"Your unique ID number is: {hash_code}")
        bucket_index = (hash_code%127)
        self.buckets[bucket_index].add(name, rating, genre, hash_code)
        return

    def search(self, key, uid):
        self.key = key
        self.uid = uid
        print("""
        Please enter a number:
        1. Search by Movie Name
        2. Search by ID""")
        ans = input()
        if ans == '1':
            key = input("Please enter movie name")
            for bucket in self.buckets:
                userid = bucket.return_id(key)
                if userid is not None:
                    bucket.findname(userid)
                    return

        elif ans == '2':
            uid = int(input("Please enter the ID number "))
            bucket_index = (uid % 127)
            return self.buckets[bucket_index].findid(uid)

        else:
            print("Invalid input")


    # def sort(self):




    def delete(self):
        uid = int(input("Please enter an ID number: "))
        bucket_index = (uid % 127)
        self.buckets[bucket_index].dlt(uid)
        return

    def save(self):
        print("""
                Please enter a number:
                1. Search by Movie Name
                2. Search by ID""")
        ans = input()
        if ans == '1':
            key = input("Please enter movie name")
            for bucket in self.buckets:
                userid = bucket.return_id(key)
                if userid is not None:
                    bucket.sve(userid)
                    return

        elif ans == '2':
            uid = int(input("Please enter the ID number: "))
            bucket_index = (uid % 127)
            self.buckets[bucket_index].sve(uid)
            return


    # def dply(self):
    #     print("Sorting and displaying all points of interest:")
    #     for i, bucket in enumerate(self.buckets):
    #         print(self.buckets[i].extract_and_sort())

    def dply(self):
        for i in range(len(self.buckets)):
            self.buckets[i].extract_and_sort()



ht = HashTable()
ht.hash('')
# ht.put('','', '')
# print(ht.search(''))

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
#Create menu
        menu = int(input())
        try:
            if menu == 1:
                ht.put('', '', '', '')
            elif menu == 2:
                 ht.search('', '')
            elif menu == 3:
                ht.delete()
            elif menu == 4:
                ht.save()
            elif menu == 5:
                ht.dply()
            elif menu == 6:
                print("Application terminated")
                break
            else:
                print("Please enter a valid menu option")

        except ValueError:
            print("Invalid input!")
        except TypeError:
            print("Invalid input!, this option does not exist")