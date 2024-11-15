from exam_node import Node


class TuplesLinkedList:
    def __init__(self):
        self.first = None
        self.last = None


    def add(self, key, value, description, hash_code):
        key_value = (key, value, description, hash_code)
        n = Node(key_value)
        if self.first is None:
            self.first = n
            self.last = n
            print(f"Succesfully added first: {n}")
        else:
            self.last.link(n)
            self.last = n
            print(f"Succesfully added: {n}")

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


    def findkey(self, searchInput):
        currentNode = self.first
        while currentNode is not None:
            if currentNode.value[0] == searchInput:
                return (f"Value: {currentNode.value[1]}, Description: {currentNode.value[2]}")
            else:
                currentNode = currentNode.next
        return

    def findid(self, id):
        currentNode = self.first
        while currentNode is not None:
            if currentNode.value[3] == id:
                print(f"Value: {currentNode.value[1]}, Description: {currentNode.value[2]}")
                return
            else:
                currentNode = currentNode.next

    def dlt(self, poi):
        currentnode = self.first
        while currentnode is not None:
            if currentnode.value[0] == poi:
                print(f" - {currentnode.value[0]} -  will be deleted")
                currentnode.delete()
                return
            else:
                currentnode = currentnode.next
        return None

    def sve(self, file_input):
        currentnode = self.first
        while currentnode is not None:
            if currentnode.value[0] == file_input:
                file_input = currentnode.value[0]
                value = currentnode.value[1]
                description = currentnode.value[2]


                tupl = [f"  Name: {(file_input)}  |  Value: {(value)}  |  Description: {(description)}  "]
                with open('poi.txt', "a") as f:
                        f.write(f'{tupl}\n')
                print(f"{tupl} will be saved")
                break

        ans = 0
        while ans != "y" and ans != "n":
            ans = input("Would you like to view saved  Points Of Interest? (y/n): ").lower()
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
        if currentnode is not None:
            while currentnode is not None:
                print(f"  Name: {currentnode.value[0]}  |  Value:  {currentnode.value[1]}  |  Description:  {currentnode.value[2]}  ")
                return currentnode.value[0], currentnode.value[1], currentnode.value[2]
        else:
            print("empty")
            return None

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

    def put(self, key, value, description, hash_code):
        self.key = key
        self.value = value
        self.description = description
        self.hash_code = hash_code
        key = input("Please enter a key")
        value = input("Please enter a value")
        description = input("Please enter a description")
        hash_code = self.hash(key)
        bucket_index = hash_code%127
        self.buckets[bucket_index].add(key, value, description, hash_code)
        print(f"ID: {hash_code}")
        return

    def search(self,key, id):
        self.key = key
        self.id = id
        print("""
        Please Enter either 1 or 2
        
        1. Search by key: 
        2. Search by ID number: """)
        ans = input()

        if ans == '1':
            key = input("Please enter a key to search")
            code = self.hash(key)
            bucket_index = code % 127
            return self.buckets[bucket_index].findkey(key)
        elif ans == '2':
            id = int(input("Please enter an ID number: "))
            bucket_index = id % 127
            return self.buckets[bucket_index].findid(id)



    def delete(self):
        poi = input("Please enter a key to delete")
        hash_code = self.hash(poi)
        bucket_index = hash_code % 127
        self.buckets[bucket_index].dlt(poi)
        return

    def save(self):
        file_input = input("Please enter a POI to save: ").lower()
        hash_code = self.hash(file_input)
        bucket_index = hash_code % 127
        self.buckets[bucket_index].sve(file_input)

    def dply(self):
        for i in range(len(self.buckets)):
                self.buckets[i].display()







ht = HashTable()
ht.hash('')
# ht.put('','', '')
# print(ht.search(''))

while True:
        print("""Please enter a number
          1. Add POI: 
          2. Search POI: 
          3. Delete POI: 
          4. Save POI: 
          5. Display POI: 
          6. Sort: 
          7. Exit: 
          ---------------
          8. Enquiries: """)
#Create menu
        menu = int(input())
        try:
            if menu == 1:
                ht.put('', '', '', '')
            elif menu == 2:
                print(ht.search('', ''))
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