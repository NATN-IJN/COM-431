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

cat1 = Cat("Binnie", 4,"British","Black")
cat1.eat(4)
cat1.walk(6)
if cat1.weight >= 1:
   print(cat1.name, cat1.weight, cat1.breed, cat1.colour)
else: print("Cat cannot walk");


cat3 = Cat("Old Tom", 6, "shortair", "bluish grey")
cat3.eat(6)
cat3.walk(5)
if cat3.weight >= 1:
   print(cat3.name, cat3.weight, cat3.breed, cat3.colour);
else:
    print("Cat cannot walk");

