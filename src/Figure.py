class Figure:

    # Инициализируем класс,присваиваем дефолтные значения и ждем аргументы из дочерних классов для валидации
    def __init__(self, *args):
        self._area = None
        self._perimeter = None
        self._name = None
        for arg in args:
            self.validate_arg(arg)

    # Складываем площадь текущего класса с классом target_class
    def add_area(self, target_class):
        if not isinstance(target_class, Figure):
            raise ValueError("Передан неправильный класс!")
        if not isinstance(self._area, (int, float)):
            raise TypeError(f"Невозможно сложить. Прощадь не является числом. Тип: {type(self._area)}")
        if not isinstance(self._perimeter, (int, float)):
            raise TypeError(f"Невозможно сложить. Периметр не является числом. Тип: {type(self._area)}")
        if not isinstance(target_class.area, (int, float)):
            raise TypeError(
                f"Невозможно сложить. Площадь у целевого класса не является числом. Тип: {type(target_class.area)}")
        return self._area + target_class.area

    @staticmethod
    def validate_arg(arg):
        if not isinstance(arg, (int, float)):
            raise TypeError(f"Ошибка вычислений. Аргумент {arg} не является числом. Тип: {type(arg)}")
        if arg < 1:
            raise ValueError("Сторона фигуры не может быть отрицательной, либо равной нулю")

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter

    @property
    def name(self):
        return self._name
