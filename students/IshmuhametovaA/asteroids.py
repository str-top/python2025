class Asteroid:
    def __init__(self, name: str, diameter_km: float, speed_kms: float):
        self.name = name
        self.diameter_km = diameter_km
        self.speed_kms = speed_kms

    def is_dangerous(self) -> bool:
        """Проверяет, является ли астероид опасным"""
        return self.diameter_km > 1000 and self.speed_kms > 25

    def display_info(self) -> None:
        """Выводит информацию об астероиде"""
        print(f"Астероид: {self.name}")
        print(f"Диаметр: {self.diameter_km} d")
        print(f"Скорость: {self.speed_kms} км/с")
        danger_status = "Да" if self.is_dangerous() else "Нет"
        print(f"Опасен: {danger_status}")
        print()


asteroids = [
    Asteroid("Церера", 950, 18),
    Asteroid("Паллада", 511, 18),
    Asteroid("Эвфросина", 268, 17),
    Asteroid("Гектар", 256, 21),
    Asteroid("Дафна", 187, 18)
]

# Выводим информацию о каждом астероиде
print("Информация об астероидах:")
for asteroid in asteroids:
    asteroid.display_info()
