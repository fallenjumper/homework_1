from src.Figure import Figure


class Square(Figure):

    def __init__(self, side):
        super().__init__(side)
        self._name = "Square"
        self.__side = side
        self.__calculate_attr()

    def __calculate_attr(self):
        self._area = self.__side ** 2
        self._perimeter = 4 * self.__side
