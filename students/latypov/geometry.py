from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def info(self):
        print(f"{self.__class__.__name__}: Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Пример использования
if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    circle = Circle(3)
    
    rectangle.info()  # Вывод: Rectangle: Area = 20.00, Perimeter = 18.00
    circle.info()     # Вывод: Circle: Area = 28.27, Perimeter = 18.85
