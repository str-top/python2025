class Vehicle:
    def __init__(self, brand, model, year, mileage=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
    
    def drive(self, distance):
        if distance > 0:
            self.mileage += distance
        else:
            print("Дистанция должна быть положительным числом")
    
    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Пробег: {self.mileage} км")


class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type, mileage=0):
        super().__init__(brand, model, year, mileage)
        self.fuel_type = fuel_type
    
    def display_info(self):
        super().display_info()
        print(f"Тип топлива: {self.fuel_type}")


class Truck(Vehicle):
    def __init__(self, brand, model, year, max_load, mileage=0, current_load=0):
        super().__init__(brand, model, year, mileage)
        self.max_load = max_load
        self.current_load = current_load
    
    def load_cargo(self, weight):
        if weight <= 0:
            print("Вес груза должен быть положительным")
            return
        
        if self.current_load + weight <= self.max_load:
            self.current_load += weight
            print(f"Груз {weight} т загружен. Текущий груз: {self.current_load} т")
        else:
            print(f"Невозможно загрузить {weight} т. Превышена максимальная грузоподъемность")
    
    def unload_cargo(self, weight):
        if weight <= 0:
            print("Вес груза должен быть положительным")
            return
        
        if self.current_load - weight >= 0:
            self.current_load -= weight
            print(f"Груз {weight} т разгружен. Текущий груз: {self.current_load} т")
        else:
            print(f"Невозможно разгрузить {weight} т. Текущий груз меньше запрошенного")
    
    def display_info(self):
        super().display_info()
        print(f"Максимальная грузоподъемность: {self.max_load} т")
        print(f"Текущий груз: {self.current_load} т")

vehicle = Vehicle("УАЗ", "Патриот", 2020)
vehicle.drive(150)
vehicle.display_info()

car = Car("Toyota", "Camry", 2022, "бензин", 5000)
car.drive(200)
car.display_info()


truck = Truck("КАМАЗ", "6520", 2019, 20)
truck.load_cargo(15)
truck.load_cargo(10) 
truck.unload_cargo(5)
truck.drive(300)
truck.display_info()
