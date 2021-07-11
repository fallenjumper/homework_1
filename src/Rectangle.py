from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a, side_b):
        super().__init__(side_a, side_b)
        self._name = "Rectangle"
        self.__side_a = side_a
        self.__side_b = side_b
        # Проверка не является ли квадратом запрошенная фигура
        if self.__side_a != self.__side_b:
            self.__calculate_attr()

    def __calculate_attr(self):
        self._area = self.__side_a * self.__side_b
        self._perimeter = 2 * self.__side_a + 2 * self.__side_b
