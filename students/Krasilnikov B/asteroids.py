class Asteroid:
    def __init__(self, name, diameter_km, speed_kms):
        self.name = name
        self.diameter_km = diameter_km
        self.speed_kms = speed_kms
    
    def is_dangerous(self):
        if self.diameter_km >= 1000 and self.speed_kms >= 25:
            return True
        else:
            return False
    
    def display_info(self):
        if self.is_dangerous():
            print(f'Астероид по имени {self.name} диаметром {self.diameter_km} км летит со скоростью {self.speed_kms} км/с опасен для нас)')
        else:
            print(f'Астероид по имени {self.name} диаметром {self.diameter_km} км летит со скоростью {self.speed_kms} км/с не представляет никакой опасности')

aster1 = Asteroid('Ignat', 911, 30)
aster2 = Asteroid('Ramdjon', 100, 60)
aster3 = Asteroid('Danil', 2651, 40)

aster1.display_info()
aster2.display_info()
aster3.display_info()
