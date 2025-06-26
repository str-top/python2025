from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    def info(self) -> str:
        return f"Площадь: {self.area():.2f}, Периметр: {self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def info(self) -> str:
        return (f"Прямоугольник: Ширина={self.width:.2f}, Высота={self.height:.2f}\n" 
                f"{super().info()}")

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def info(self) -> str:
        return (f"Круг: Радиус={self.radius:.2f}\n"
                f"{super().info()}")

if __name__ == "__main__":
    rectangle = Rectangle(7, 4)
    print(rectangle.info())
    
    print()
    
    circle = Circle(6)
    print(circle.info())
