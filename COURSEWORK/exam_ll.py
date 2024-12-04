from node import Node

class TupleLinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, key, value, description):
        self.key = key
        self.value = value
        self.description = description
        key = input("Please enter a key: ").lower()
        value = input("Please enter a value: ")
        description = input("Please enter a description: ")
        tupl = (key, value, description)
        new_node = Node(tupl)
        if self.head is None:
            self.head = Node(tupl)
            self.tail = Node(tupl)
            print(f"Succesfully added first: {new_node}")
            return
        else:
            self.tail.link(new_node)
            self.tail.next = new_node
            print(f"Succesfully added: {new_node}")
            return


    def find(self):
        searchinput = input("Please enter a key to search: ").lower()
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
        file_input = input("Please enter a POI to save: ").lower()
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


    def display(self):
        currentnode = self.head
        if currentnode is not None:
            while currentnode is not None:
                print(f"  Name: {currentnode.value[0]}  |  Value:  {currentnode.value[1]}  |  Description:  {currentnode.value[2]}  ")

                return currentnode.value[0], currentnode.value[1], currentnode.value[2]
        else:
            print("Database empty")
            return None



tll = TupleLinkedLists()
# tll.add('', '', '' )
# tll.display()
# tll.find()
# tll.save(file_input='poi.txt')
# tll.dlt()


while True:
        print("""Please enter a number
          1. Add POI
          2. Search POI
          3. Delete POI
          4. Save POI
          5. Display POI
          6. Exit""")
#Create menu
        menu = int(input())
        try:
            if menu == 1:
                tll.add('', '', '')
            elif menu == 2:
                tll.find()
            elif menu == 3:
                tll.dlt()
            elif menu == 4:
                tll.save(file_input='poi.txt')
            elif menu == 5:
                tll.display()
            elif menu == 8:
                print("Application terminated")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number")
        except TypeError:
            print("Invalid input! Please enter a number")





