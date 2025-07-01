class Asteroid:
    def __init__(self, name, diameter_km, speed_kms):
        self.name = name
        self.diameter_km = diameter_km
        self.speed_kms = speed_kms

    def is_dangerous(self):
        return self.diameter_km > 1000 and self.speed_kms > 25

    def display_info(self):
        danger_status = "Опасен" if self.is_dangerous() else "Не опасен"
        print(f"Астероид: {self.name}")
        print(f"Диаметр: {self.diameter_km} км")
        print(f"Скорость: {self.speed_kms} км/с")
        print(f"Статус: {danger_status}\n")

asteroids = [
    Asteroid("Apophis", 370, 30),
    Asteroid("Bennu", 500, 20),
    Asteroid("Vesta", 530, 26)
]

for asteroid in asteroids:
    asteroid.display_info()
