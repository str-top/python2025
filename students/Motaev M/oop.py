class Pet:
    def __init__(self, name: str, animal_type: str, hunger: int = 0):
        self.name = name
        self.animal_type = animal_type
        self.hunger = max(0, min(hunger, 10)) 

    def feed(self) -> None:
        self.hunger = max(0, self.hunger - 2)

    def play(self) -> None:
        self.hunger = min(10, self.hunger + 1)

    def get_status(self) -> str:
        return f"{self.animal_type.capitalize()} {self.name} (голод: {self.hunger}/10)" 
        
my_pet = Pet("Барбос", "Собака", 3)

my_pet.feed()  
my_pet.play()  

print(my_pet.get_status())  
