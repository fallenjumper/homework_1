from math import sqrt
from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        super().__init__(side_a, side_b, side_c)
        self._name = "Triangle"
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        # Проверка возможности создания треугольника по заданным аргументам
        if (self.__side_a + self.__side_b > self.__side_c) and (self.__side_a + self.__side_c > self.__side_b) \
                and (self.__side_b + self.__side_c > self.__side_a):
            self.__calculate_attr()

    def __calculate_attr(self):
        self._perimeter = self.__side_a + self.__side_b + self.__side_c
        half_perimeter = self.perimeter / 2
        self._area = int(
            sqrt(half_perimeter * (half_perimeter - self.__side_a) * (half_perimeter - self.__side_b) * (
                    half_perimeter - self.__side_c)))
