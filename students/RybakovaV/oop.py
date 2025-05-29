class Pet:
    def __init__(self, name: str, animal_type: str, hunger: int = 5, energy: int = 5):
        self.name = name
        self.animal_type = animal_type
        self.hunger = max(0, min(hunger, 10))  
        self.energy = max(0, min(energy, 10)) 

    def feed(self) -> None:
        """Уменьшает уровень голода на 2 (но не меньше 0)."""
        self.hunger = max(0, self.hunger - 2)
        print(f"{self.name} покормлен. Уровень голода: {self.hunger}/10")

    def play(self) -> None:
        """Увеличивает уровень голода на 1 (но не больше 10)."""
        self.hunger = min(10, self.hunger + 1)
        print(f"Вы поиграли с {self.name}. Уровень голода: {self.hunger}/10")

    def sleep(self, hours: int = 1) -> None:
        """Восстанавливает энергию (1 единица за 1 час сна)."""
        self.energy = min(10, self.energy + hours)
        print(f"{self.name} поспал {hours} ч. Энергия: {self.energy}/10")

    def run(self) -> None:
        """Тратит энергию (1 единицу за 1 пробежку)."""
        if self.energy > 0:
            self.energy = max(0, self.energy - 1)
            self.hunger = min(10, self.hunger + 1)  # Бег увеличивает голод
            print(f"{self.name} побегал. Энергия: {self.energy}/10, голод: {self.hunger}/10")
        else:
            print(f"{self.name} слишком устал для бега!")

    def get_status(self) -> str:
        """Возвращает строку с информацией о животном."""
        return f"{self.animal_type} {self.name} (голод: {self.hunger}/10, энергия: {self.energy}/10)"
cat = Pet("Барсик", "Кот", hunger=3, energy=8)
print(cat.get_status())
cat.feed() 
cat.play() 
print(cat.get_status()) 
cat.run() 
cat.sleep(2)
