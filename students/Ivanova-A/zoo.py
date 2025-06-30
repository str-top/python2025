class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
  
    def make_sound(self):
        print(f"{self.name} издаёт звук: {self.sound}")
  
    def info(self):
        print(f"Кличка: {self.name}\nВид: {self.species}\nВозраст: {self.age}\nИздаёт звук: {self.sound}")


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное '{animal.name}' добавлено в зоопарк.")

    def show_animals(self):
        print("\nСписок животных в зоопарке:")
        for animal in self.animals:
            animal.info()
            print()

    def make_all_sounds(self):
        print("\nЗвуки животных:")
        for animal in self.animals:
            animal.make_sound()


zoo = Zoo()

a = Animal("Инокентий", "Лев", 8, "Рррр!")
p = Animal("Тригг", "Волк", 1, "Аууу!")

zoo.add_animal(a)
zoo.add_animal(p)

zoo.show_animals()

zoo.make_all_sounds()
