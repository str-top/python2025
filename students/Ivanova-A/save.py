import json

class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age
    
    def __str__(self):
        return f"Имя: {self.name}, Вид: {self.animal_type}, Возраст: {self.age} лет"
    
    def to_dict(self):
        return {
            'name': self.name,
            'animal_type': self.animal_type,
            'age': self.age
        }
    
    @staticmethod
    def from_dict(data):
        return Pet(data['name'], data['animal_type'], data['age'])

def save_to_file(pets):
    try:
        with open('pets.json', 'w', encoding='utf-8') as file:
            json_data = [pet.to_dict() for pet in pets]
            json.dump(json_data, file, ensure_ascii=False, indent=2)
        print("Данные успешно сохранены в файл pets.json")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

def load_from_file():
    pets = []
    try:
        with open('pets.json', 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            pets = [Pet.from_dict(item) for item in json_data]
        print("Данные успешно загружены из файла pets.json")
    except FileNotFoundError:
        print("Файл pets.json не найден. Создан новый список.")
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")
    
    return pets

def add_pet(pets):
    print("\n--- Добавление питомца ---")
    name = input("Имя питомца: ").strip()
    animal_type = input("Вид животного: ").strip()
    
    try:
        age = int(input("Возраст (лет): "))
        if age < 0:
            print("Возраст не может быть отрицательным!")
            return
    except ValueError:
        print("Возраст должен быть числом!")
        return
    
    pets.append(Pet(name, animal_type, age))
    print(f"Питомец {name} добавлен!")

def show_pets(pets):
    print("\n--- Список питомцев ---")
    if not pets:
        print("Питомцев нет")
        return
    
    for i, pet in enumerate(pets, 1):
        print(f"{i}. {pet}")

def main():
    pets = []
    
    while True:
        print("\n" + "="*40)
        print("Учет питомцев")
        print("="*40)
        print("1. Добавить питомца")
        print("2. Сохранить в файл")
        print("3. Загрузить из файла")
        print("4. Показать всех питомцев")
        print("0. Выход")
        
        choice = input("Выберите действие: ").strip()
        
        if choice == '1':
            add_pet(pets)
        elif choice == '2':
            save_to_file(pets)
        elif choice == '3':
            pets = load_from_file()
        elif choice == '4':
            show_pets(pets)
        elif choice == '0':
            print("Выход из программы")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
