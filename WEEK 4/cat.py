class Cat:
    def __init__(self, name, weight, breed, colour):
        self.name = name
        self.weight = weight
        self.breed = breed
        self.colour = colour

    def eat(self, amount):
        self.weight += amount
    def walk(self, distance):
        self.weight -= distance



