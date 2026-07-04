class LivingThing:
    def __init__(self, living_status):
        self.living_status = living_status
class Animal(LivingThing):
    def __init__(self, living_status, species):
        super().__init__(living_status)
        self.species = species
class Dog(Animal):
    def __init__(self, living_status, species, breed):
        super().__init__(living_status, species)
        self.breed = breed
    def display(self):
        print("Living Status :", self.living_status)
        print("Species       :", self.species)
        print("Breed         :", self.breed)

d = Dog("Alive", "Mammal", "Labrador")
d.display()