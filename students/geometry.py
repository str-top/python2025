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
        """Вывод информации о фигуре"""
        print(f"Площадь: {self.area():.2f}")
        print(f"Периметр: {self.perimeter():.2f}")
      
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

if __name__ == "__main__":
    rect = Rectangle(4, 5)
    circle = Circle(3)

    print("Прямоугольник:")
    rect.info()

    print("\nКруг:")
    circle.info()
