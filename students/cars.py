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
            print("Расстояние должно быть положительным числом.")

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
    def __init__(self, brand, model, year, max_load, current_load=0, mileage=0):
        super().__init__(brand, model, year, mileage)
        self.max_load = max_load
        self.current_load = current_load

    def load_cargo(self, weight):
        if weight <= 0:
            print("Вес груза должен быть положительным числом.")
            return
        if self.current_load + weight <= self.max_load:
            self.current_load += weight
            print(f"Загружено {weight} тонн. Текущий груз: {self.current_load} тонн.")
        else:
            print("Превышен максимальный грузоподъемность!")

    def unload_cargo(self, weight):
        if weight <= 0:
            print("Вес разгружаемого груза должен быть положительным числом.")
            return
        if weight <= self.current_load:
            self.current_load -= weight
            print(f"Разгружено {weight} тонн. Текущий груз: {self.current_load} тонн.")
        else:
            print("Невозможно разгрузить больше текущего груза!")

    def display_info(self):
        super().display_info()
        print(f"Максимальная грузоподъемность: {self.max_load} тонн")
        print(f"Текущий груз: {self.current_load} тонн")

if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2020, "бензин")
    car.display_info()
    car.drive(150)
    print("\nПосле поездки:")
    car.display_info()

    truck = Truck("Volvo", "FH", 2018, max_load=20)
    truck.display_info()
    truck.load_cargo(5)
    truck.load_cargo(16)
    truck.unload_cargo(2)
    print("\nПосле загрузки и разгрузки:")
    truck.display_info()
