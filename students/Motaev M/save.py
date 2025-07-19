import json

# Класс Pet
class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def to_dict(self):
        return {
            'name': self.name,
            'animal_type': self.animal_type,
            'age': self.age
        }

    @staticmethod
    def from_dict(data):
        return Pet(data['name'], data['animal_type'], data['age'])

pets = []

def save_to_file(pets_list):
    with open('pets.json', 'w', encoding='utf-8') as f:
        json.dump([pet.to_dict() for pet in pets_list], f, ensure_ascii=False, indent=4)
    print("Данные успешно сохранены в pets.json.")

def load_from_file():
    global pets
    try:
        with open('pets.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            pets = [Pet.from_dict(item) for item in data]
        print("Данные успешно загружены из pets.json.")
    except FileNotFoundError:
        print("Файл pets.json не найден. Загружать нечего.")
    except json.JSONDecodeError:
        print("Ошибка чтения файла. Проверьте формат данных.")

def add_pet():
    name = input("Введите имя питомца: ")
    animal_type = input("Введите вид животного (например, кошка, собака): ")
    while True:
        try:
            age = int(input("Введите возраст: "))
            break
        except ValueError:
            print("Пожалуйста, введите числовое значение для возраста.")
    pet = Pet(name, animal_type, age)
    pets.append(pet)
    print(f"Питомец {name} добавлен.")

def show_pets():
    if not pets:
        print("Список питомцев пуст.")
        return
    for idx, pet in enumerate(pets, start=1):
        print(f"{idx}. Имя: {pet.name}, Вид: {pet.animal_type}, Возраст: {pet.age}")

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить питомца")
        print("2. Сохранить в файл")
        print("3. Загрузить из файла")
        print("4. Показать всех питомцев")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_pet()
        elif choice == '2':
            save_to_file(pets)
        elif choice == '3':
            load_from_file()
        elif choice == '4':
            show_pets()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
