class Asteroid:
    def __init__(self, name, diameter_km, speed_kms):
        self.name = name
        self.diameter_km = diameter_km
        self.speed_kms = speed_kms
    
    def is_dangerous(self):
      return self.diameter_km > 1000 and self.speed_kms > 25

    def display_info(self):
      print(f"астероид: {self.name}")
      print(f"диаметр: {self.diameter_km} км")
      print(f"скорость: {self.speed_kms} км/с")
      if self.is_dangerous():
        danger_status = "опасен"
      else:
        danger_status = "не опасен"
      print(f"статус: {danger_status}\n")

asteroids = [
    Asteroid("Церера", 950, 10),
    Asteroid("Веста", 525, 30)
]
for asteroid in asteroids:
    asteroid.display_info()
