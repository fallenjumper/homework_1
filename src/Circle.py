from src.Figure import Figure
from math import pi


class Circle(Figure):

    def __init__(self, radius):
        super().__init__(radius)
        self._name = "Circle"
        self.__radius = radius
        self.__calculate_attr()

    def __calculate_attr(self):
        self._area = pi * self.__radius ** 2
        self._perimeter = 2 * pi * self.__radius
