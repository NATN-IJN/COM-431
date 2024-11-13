from exam_node import Node

class TupleLinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, key, value):
        self.key = key
        self.value = value
        key = input("Please enter a key: ")
        value = input("Please enter a value: ")
        description = input("Please enter a description: ")
        tupl = (key, value, description)
        new_node = Node(tupl)
        if self.head is None:
            self.head = Node(tupl)
            self.tail = Node(tupl)
            print(f"Succesfully added: {new_node}")
            return
        else:
            self.tail.link(new_node)
            self.tail = new_node
            return


    def find(self):
        searchinput = input("Please enter a key to search: ")
        currentnode = self.head
        while currentnode is not None:
            if currentnode.value[0] == searchinput:
                print(f"Value: {currentnode.value[1]}, Description: {currentnode.value[2]}")
                return currentnode.value[1], currentnode.value[2]
            else:
                currentnode = currentnode.next
        return None

    def save(self, file_input):
        self.file_input = file_input
        file_input = input("Please enter a POI to save: ")
        currentnode = self.head
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

    def dlt(self):
        del_input = input("Please enter the Point of interest to delete: ")
        currentnode = self.head
        while currentnode is not None:
            if currentnode.value[0] == del_input:
                print(f" - {currentnode.value[0]} -  will be deleted")
                currentnode.delete()
                return
            else:
                currentnode = currentnode.next
        return None

    # def sort(self):
    #     print("Sorting...")








tll = TupleLinkedLists()
tll.add('cat', 'meow')
tll.find()
tll.save(file_input='poi.txt')
tll.dlt()

