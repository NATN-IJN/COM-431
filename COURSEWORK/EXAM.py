#Create class: this will act as the database for the POIs
from exam_node import Node
class PointOfInterest:
    def __init__(self):
        self.pois = []

#Create method to add POIs
    def add_poi (self, poi=None):
        if poi is None:
            name = input("Enter the name of the POI: ")
            type_poi = input("Enter the type of POI: ")
            description = input("Enter the description of the POI: ")
            new_poi={"Name": name, "Type": type_poi, "Description": description}
            self.pois.append(new_poi)
            return f"{new_poi} has been added"
        else:
            self.pois.append(poi)
            return f"{poi} has been added \t"





    def search_poi(self):
        pass

    def delete_poi(self):
        pass

    def save_poi(self):
        pass

    def display_poi(self):
        print(self.pois)


    def __str__(self):
        return str(self.pois)

if __name__ == "__main__":
    run = PointOfInterest()

#While loop
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
               print(run.add_poi())
            elif menu == 5:
                print(run.display_poi())
            elif menu == 6:
                print("Application terminated")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number")
        except TypeError:
            print("Invalid input! Please enter a number")