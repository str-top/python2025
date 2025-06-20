class Asteroid:
  def __init__(self, name:str, diameter_km:int, speed_kms:int):
    self.name = name
    self.diameter_km =diameter_km
    self.speed_kms = speed_kms
  def  is_dangerous(self):
    if self.diameter_km > 1000 and self.speed_kms > 25:
      return True
    return False
  def display_info(self):
        print(f"Имя - {self.name}")
        print(f"Диаметр - {self.diameter_km}")
        print(f"Скорость - {self.speed_kms}")
        print(f"Опасность - {self.is_dangerous()}")
        

a1 = Asteroid("sdd", 12, 12)
a2 = Asteroid("sass", 1001, 27)
a3 = Asteroid("dsa", 112, 29)
asteroids = [a1, a2, a3]

for i, asteroid in enumerate(asteroids, 1):
    print(f'\nХарактеристика {i} метеора')
    asteroid.display_info()
