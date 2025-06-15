from abc import ABC, abstractmethod
import math
class Shape(ABC):
  @abstractmethod
  def area(self):
    pass
  @abstractmethod
  def perimeter(self):
    pass
  @abstractmethod
  def info(self):
    print(f"фигура: {self.__class__.__name__}")
    print(f"площадь: {self.area():.2f}")
    print(f"периметр/длина окружности: {self.perimeter():.2f}")

class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

  def perimeter(self):
    return 2 * (self.width + self.height)

  def info(self):
    super().info()
    print(f"Ширина: {self.width}, Высота: {self.height}")

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
  def area(self):
    return math.pi * self.radius ** 2
  def perimeter(self):
    return 2 * math.pi * self.radius
  def info(self):
    super().info()
    print(f"Радиус: {self.radius}")
rect = Rectangle(5, 3)
rect.info()
circl = Circle(5)
circl.info()
