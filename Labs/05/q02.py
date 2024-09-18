from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return 0.5 * self.length * self.height
    
print(
    f"square: {Square(10).area()}",
    f"rectangle: {Rectangle(10, 12).area()}",
    f"triangle: {Triangle(10, 10).area()}",
    sep='\n'
)
