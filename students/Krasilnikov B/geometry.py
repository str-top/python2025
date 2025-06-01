from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area():
        pass    
    
    @abstractmethod
    def perimeter():
        pass    
    
    def info(self):
        self.area()
        self.perimeter()
    
    
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def area(self):
        s = self.a * self.b
        print(f'площадь прямоугольника равна {s}')
    
    def perimeter(self):
        p = (self.a + self.b) * 2
        print(f'периметр прямоугольника равен {p}')
        

        
pryamougol = Rectangle(2, 2)

pryamougol.info()


class Circle(Shape):
    
    pi = 3.1428
    def __init__(self,r):
        self.r = r
        

    def area(self):
        s = self.pi *(self.r * self.r)
        print(f'площадь прямоугольника равна {s}')
    
    def perimeter(self):
        p = 2 * self.pi * self.r
        print(f'периметр прямоугольника равен {p}')
    


circle = Circle(4)
circle.info()
