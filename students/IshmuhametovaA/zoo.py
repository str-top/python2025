class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
    
    def make_sound(self):
        print(f'{self.species} говорит {self.sound}!')
        
    
    def info(self):
        print(f'''
        Кличка:{self.name}
        Вид:{self.species}
        Возраст:{self.age}
        ''')
        

class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self,animal):
        self.animals.append(animal)
        
    def show_animals(self):
        for animal in self.animals:
            animal.info()
    def make_all_sounds(self):
        for animal in self.animals:
            animal.make_sound()
            
lion = Animal('barsik', 'lion', 5, 'arrrrw')


cat = Animal('Jessie', 'cat', 7, 'mew')
dog = Animal('Jack', 'dog', 4, 'gav')
zoo = Zoo()

zoo.add_animal(lion)
zoo.add_animal(dog)
zoo.add_animal(cat)
zoo.show_animals()
zoo.make_all_sounds()
