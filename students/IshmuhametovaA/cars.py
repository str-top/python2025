class Vehicle:
    
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        
    
    def drive(self, distance):
        self.mileage += distance
        print(f'пробег увеличился на {distance}, теперь пробег равен {self.mileage} км')
        
    def display_info(self):
        print(f'''
            Марка: {self.brand}
            Модель: {self.model}
            Год выпуска: {self.year}
            Пробег: {self.mileage}
        ''')
        

class Car(Vehicle):

    def __init__(self, brand, model, year, mileage,fuel_type):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage 
        self.fuel_type = fuel_type
    
    def display_info(self):
        print(f'''
            Марка: {self.brand}
            Модель: {self.model}
            Год выпуска: {self.year}
            Пробег: {self.mileage}
            Тип топлива: {self.fuel_type}
        ''')
banan = Car('Lamborghini', 'Urus', 2018, 7600, 'Бензин')
banan.display_info()
banan.drive(263)
banan.display_info()
        
class Truck(Vehicle):

    def __init__(self, brand, model, year, mileage, max_load, current_load=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage 
        self.max_load = max_load
        self.current_load = current_load
    
    def display_info(self):
        print(f'''
            Марка: {self.brand}
            Модель: {self.model}
            Год выпуска: {self.year}
            Пробег: {self.mileage}
            Мвксимальная грузоподъемность на: {self.max_load} тонн(ы)
            Загружен на: {self.current_load} тонн(ы)
            ''')
    
    def load_cargo(self, weight):
        if (weight + self.current_load) > self.max_load:
            if self.current_load == 0:
                print(f'''
                У грузовика {self.brand} максимальная грузоподъемность не больше {self.max_load}
                вы пытаетесь загрузить {weight}, необходимо уменьшить груз до {self.max_load} тонн(ы)
                ''')
            else:
                print(f'''
                У грузовика {self.brand} максимальная грузоподъемность не больше {self.max_load}
                он уже загружен на {self.current_load} и вы пытаетесь еще загрузить {weight}, необходимо уменьшить груз до {self.max_load - self.current_load} тонн
                ''')
        else:
            self.current_load += weight
            print(f'вы загрузили {weight}, теперь грузовик загружен на {self.current_load}/{self.max_load} тонн(ы)')

    def unload_cargo(self,weight):
        if self.current_load == 0:
            print(f'грузовик и так пуст, вы не можете еще больше опустошить его')
        elif (self.current_load - weight) < 0:
            print(f'вы пытаетесь разгрузить больше чем есть в грузовике, он загружен на {self.current_load} тонн(ы)')
        elif (self.current_load - weight) == 0:
            print(f'вы полностью разгрузили грузовик, теперь он пустой))')
        else:
            self.current_load -= weight
            print(f'вы разгрузили грузовик на {weight}, в нем осталось {self.current_load} тонн(ы)')


man = Truck('HOWO', 'HW 76', 2007,244000,25,10)
man.display_info()

man.unload_cargo(60)
man.display_info()
