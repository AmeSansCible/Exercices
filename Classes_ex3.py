class Pet:
    def __init__(self, name, family, animal_type, color):
        self.name = name
        self.family = family
        self.animal_type = animal_type
        self.color = color


rio = Pet("Rio", "Macaw", "Parrot", "Blue")
coco = Pet("Coco", "Poodle", "Dog", "White")
bud = Pet("Bud", "Labrador", "Dog", "Brown")
daisy = Pet("Daisy", "Burmese", "Cat", "Grey")
print(f"{rio.name} is a {rio.color} colored {rio.family} {rio.animal_type}")