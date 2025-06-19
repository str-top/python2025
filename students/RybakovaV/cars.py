class Vehicle:
    def __init__(self, brand, model, year, mileage=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
    def drive(self, distance):
      if distance > 0:
        self.mileage += distance
        print(f"Проехали {distance} км. Общий пробег:  {self.mileage} км.")
      else:
        print("Ошибка, расстояние должно быть положительным")
    def display_info(self):
      print(f"Марка: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.year}\nПробег: {self.mileage} км")

class Car(Vehicle):
  def __init__(self, brand, model, year,fuel_type, mileage=0):
    super().__init__(brand, model, year,mileage)
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
    if weight > 0:
      if self.current_load + weight <= self.max_load:
        self.current_load += weight
        print(f"Груз загружен. Текущая нагрузка: {self.current_load} т")
      else:
        print(f"Превышена максимальная грузоподъемность. Максимум: {self.max_load} т")
  def unload_cargo(self, weight):
    if weight > 0:
      if self.current_load - weight >= 0:
        self.current_load -= weight
        print(f"Груз разгружен. Текущая нагрузка: {self.current_load} т")
      else:
        print("Нельзя разгрузить больше, чем есть сейчас")
    
  def display_info(self):
    super().display_info()
    print(f"Максимальная грузоподъемность: {self.max_load} т")
    print(f"Текущая нагрузка: {self.current_load} т")

car = Car("Toyota", "Camry", 2020, "бензин")
car.drive(150)
car.display_info()
truck = Truck("Volvo", "FH16", 2018, 20)
truck.drive(500)
truck.load_cargo(15)
truck.load_cargo(10) 
truck.unload_cargo(5)
truck.display_info()
