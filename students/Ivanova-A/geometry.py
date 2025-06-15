from abc import ABC, abstractmethod
class Shape (ABC):
  @abstractmethod
  def area(self):
    pass
  @abstractmethod
  def perimeter(self):
    pass
  def info(self):
    print(f"{self.__class__.__name__}: Area = {self.area()}, Perimeter = {self.perimeter()}")
 
class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height
   
  def area(self):
    return self.width * self.height
  
  def perimeter(self):
    return (self.width + self.height) * 2 

class Circle(Shape):

  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return 3.14 * self.radius**2
  
  def perimeter(self):
    return 2 * 3.14 *self.radius

retagle = Rectangle(12, 4)
circle = Circle(6)
print(circle.area())
print(retagle.perimeter())
print(retagle.area())
