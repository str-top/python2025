class Animal:
    def __init__(self, name, species, age):
        
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        
        if self.species == "лев":
            print("ррр")
        elif self.species == "кот":
            print("мяу")
        elif self.species == "собака":
            print("гав гав")
        else:
            print("Звук животного")

    def info(self):
        
        print(f"Кличка: {self.name}")
        print(f"Вид: {self.species}")
        print(f"Возраст: {self.age} лет")


class Zoo:
    def __init__(self):
        
        self.animals = []

    def add_animal(self, animal):
        
        self.animals.append(animal)

    def show_animals(self):
       
        if not self.animals:
            print("В зоопарке нет животных.")
        else:
            print("Животные в зоопарке:")
            for animal in self.animals:
                animal.info()

    def make_all_sounds(self):
        
        if not self.animals:
            print("В зоопарке нет животных, чтобы издать звук.")
        else:
            print("Животные издают звуки:")
            for animal in self.animals:
                print(f"{animal.name}: ", end="")
                animal.make_sound()
zoo = Zoo()
lion = Animal("симба", "лев", 7)
cat = Animal("барсик", "кот", 10)
dog = Animal("шарик", "собака", 5)
zoo.add_animal(lion)
zoo.add_animal(cat)
zoo.add_animal(dog)
zoo.show_animals()
zoo.make_all_sounds()
