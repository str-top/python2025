import json

class Pet:
  def __init__(self, name, animal_type, age):
    self.name = name
    self.animal_type = animal_type
    self.age = age

  def to_dict(self):
    return{
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
    self.save_to_file()

  def save_to_file(self):
    data = []   
    for pet in self.pets:
      data.append(pet.to_dict())
    with open("pets.json", "w") as f:
      json.dump(data, f)
  
  def load_from_file(self):
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

pet1 = Pet('Baks','Cat',3)
pet2 = Pet('Bublik','Dog',1)
pet3 = Pet('Pupsik','Cat',9)
pets.new_pet(pet1)
pets.new_pet(pet2)
pets.new_pet(pet3)

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
    animal_type = input('Кто он?(кот, собака?)')
    age = int(input('Сколько лет?'))
    pets.new_pet(Pet(name, animal_type, age))
  elif act == 2:
    pets.save()
    print('список питомцев загружен в файл pets.json')
  elif act == 3:
    pets.load()
  elif act == 4:
     pets.display_info()
  elif act == 0:
     break
