class ZooAssistant: 
    def __init__(self): 
        self.animals = {} 
        self.slides = {}  # Добавляем словарь для хранения информации о горках 

    def add_animal(self, animal_type, name): 
        if animal_type.lower() not in ['млекопитающее', 'птица', 'рептилия']: 
            print("Неверно указан тип животного.") 
            return False 
        if name in self.animals: 
            print("Животное с таким именем уже добавлено.") 
            return False 
        self.animals[name] = {'type': animal_type, 'fed_count': 0} 
        return True 

    def feed_animal(self, name): 
        if name not in self.animals: 
            print(f"Животное {name} не найдено.") 
            return 
        self.animals[name]['fed_count'] += 1 
        print(f"{self.animals[name]['type']} {name} сегодня покормили {self.animals[name]['fed_count']} раз(а)") 

    def display_all(self): 
        for name, details in self.animals.items(): 
            print(f"{details['type']} {name} сегодня покормили {details['fed_count']} раз(а)") 
        for slide_name, _ in self.slides.items(): 
            print(f"Горка {slide_name}") 

    def delete_slide(self, slide_name): 
        if slide_name in self.slides: 
            del self.slides[slide_name] 
            print(f"Горка {slide_name} была успешно удалена.") 
        else: 
            print(f"Горка {slide_name} не найдена.") 

    def add_slide(self, slide_name): 
        if slide_name in self.slides: 
            print(f"Горка с таким именем уже существует.") 
            return False 
        self.slides[slide_name] = "Информация о горке" 
        print(f"Горка {slide_name} успешно добавлена.") 

def main(): 
    assistant = ZooAssistant() 
    while True: 
        action = input("Введите действие (add, feed, display, delete_slide, add_slide, stop): ").lower() 
        if action == 'add': 
            animal_type = input("Введите тип животного (млекопитающее, птица, рептилия): ") 
            name = input("Введите имя животного: ") 
            if assistant.add_animal(animal_type, name): 
                print("Животное успешно добавлено.") 
        elif action == 'feed': 
            name = input("Введите имя животного для кормления: ") 
            assistant.feed_animal(name) 
        elif action == 'display': 
            assistant.display_all() 
        elif action == 'delete_slide': 
            slide_name = input("Введите имя горки для удаления: ") 
            assistant.delete_slide(slide_name) 
        elif action == 'add_slide': 
            slide_name = input("Введите имя новой горки: ") 
            assistant.add_slide(slide_name) 
        elif action == 'stop': 
            print("Выход из программы.") 
            break 
        else: 
            print("Неизвестная команда.") 

if __name__ == "__main__": 
    main()
