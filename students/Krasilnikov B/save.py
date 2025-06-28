import json

class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age
    
    def to_dict(self):
        return {
            "Кличка": self.name,
            "Вид": self.animal_type,
            "Возраст": self.age
        }        
    @classmethod
    def from_dict(cls, data):
        return cls(data["Кличка"], data["Вид"], data["Возраст"])

class Pets:
    pets = []
    def new_pet(self,pet):
       self.pets.append(pet)
       self.save()
        
            
    def save(self):
        data = []   
        for pet in self.pets:
            data.append(pet.to_dict())
        with open("pets.json", "w") as f:
            json.dump(data, f)
        
    def load(self):
        with open("pets.json", "r") as f:
            data = json.load(f)
        self.pets = []
        for anim in data:
            pet = Pet.from_dict(anim)
            self.pets.append(pet)
        print(data)

    def display_info(self):
        for pet in self.pets:
            print(f'''
            Кличка: {pet.name}
            Вид: {pet.animal_type}
            Возраст: {pet.age}
            ''')
            
pets = Pets()
            
pet1 = Pet('Rocket','Enot',33)
pet2 = Pet('Garik','Cat',1)
pet3 = Pet('Omela','Dog',9)
pet4 = Pet('Gavr','Dog',12)
pet5 = Pet('Almas','Cat',9)
pets.new_pet(pet1)
pets.new_pet(pet2)
pets.new_pet(pet3)
pets.new_pet(pet4)
pets.new_pet(pet5)


while True:
    act = int(input(f'''
        Что будем делать?
    1. Добавить питомца
    2. Сохранить в файл
    3. Загрузить из файла
    4. Показать всех питомцев
    0. Выход
    
    
    '''))
    if act == 1:
        name = input('Как его зовут?')
        animal_type = input('Хто он?(кот дог или лев)')
        age = int(input('Скильки лет?'))
        pets.new_pet(Pet(name, animal_type, age))
    elif act == 2:
        pets.save()
        print('спимок питомцев загружен в файл pets.json')
    elif act == 3:
        pets.load()
    elif act == 4:
        pets.display_info()
    elif act == 0:
        break
        
