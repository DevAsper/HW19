class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says chirp.")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} says roar.")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} says hiss.")
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Employee:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}")

class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}")

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the zoo.")

    def add_staff(self, employee):
        self.staff.append(employee)
        print(f"Added {employee.name} to the zoo staff.")

zoo = Zoo()

bird = Bird("Tweety", 2)
mammal = Mammal("Simba", 3)
reptile = Reptile("Slither", 4)

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

keeper = ZooKeeper("John")
vet = Veterinarian("Alice")

zoo.add_staff(keeper)
zoo.add_staff(vet)

animals = zoo.animals
animal_sound(animals)

keeper.feed_animal(mammal)
vet.heal_animal(bird)
