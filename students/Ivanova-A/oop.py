class Pet:
  def __init__(self, name, animal_type, hunger):
    self.name = name
    self.animal_type = animal_type
    self.hunger = hunger
  
  def feed(self,):
    value = int(input("Введите кол-во еды (1 - 10)"))
    print("Кормим животное...")
    self.hunger = self.hunger - value
    if self.hunger > 10:
      self.hunger = 0
    elif self.hunger < 0:
      self.hunger = 0
    print(f"Текущий голод - {self.hunger}")

  def play(self,):
    print("Играем с животным...")
    self.hunger+=1
    if self.hunger > 10:
      self.hunger = 10
    print(f"Текущий голод - {self.hunger}")

  def get_status(self):
    print(f"{self.animal_type} {self.name}, (голод {self.hunger}/10) ")

p = Pet("Марк", "Корова", 10)
p.feed()
p.play()
p.get_status()
