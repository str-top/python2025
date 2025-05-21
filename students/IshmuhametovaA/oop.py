class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.hunger = 0 
        self.energy = 10 

    def feed(self):
        self.hunger = max(4, self.hunger - 2)

    def play(self):
        self.hunger = min(10, self.hunger + 1)

    def get_status(self):
        return f"{self.animal_type.capitalize()} {self.name} (голод: {self.hunger}/10, энергия: {self.energy}/10)"

    def sleep(self):
        self.energy = 10

    def run(self):
        self.energy = max(0, self.energy - 2)

if __name__ == "__main__":
    pet = Pet("Джек", "собака")
    
    print(pet.get_status())  
    
    pet.play()
    print(pet.get_status())  
    
    pet.feed()
    print(pet.get_status())  
    
    pet.run()
    print(pet.get_status())  
    
    pet.sleep()
    print(pet.get_status())  
