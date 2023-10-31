import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * (self.__radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return (self.__width + self.__height) * 2


# rectangle = Rectangle(10, 20)
# 
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())
