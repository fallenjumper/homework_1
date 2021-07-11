import pytest
from src import *


class WrongClass:
    pass


def test_add_area_circle(default_circle, default_rectangle, default_square, default_triangle):
    # sum with correct classes
    assert default_circle.add_area(default_circle) == 628.3185307179587
    assert default_circle.add_area(default_rectangle) == 514.1592653589794
    assert default_circle.add_area(default_square) == 414.1592653589793
    assert default_circle.add_area(default_triangle) == 365.1592653589793

    # sum with other class
    with pytest.raises(ValueError):
        default_circle.add_area(WrongClass)
    # sum with err target class
    with pytest.raises(TypeError):
        default_circle.add_area(Triangle(1, 12, 13))


def test_add_area_rectangle(default_circle, default_rectangle, default_square, default_triangle):
    # sum with correct classes
    assert default_rectangle.add_area(default_circle) == 514.1592653589794
    assert default_rectangle.add_area(default_rectangle) == 400
    assert default_rectangle.add_area(default_square) == 300
    assert default_rectangle.add_area(default_triangle) == 251

    # sum with other class
    with pytest.raises(ValueError):
        default_rectangle.add_area(WrongClass)
    # sum with err target class
    with pytest.raises(TypeError):
        default_rectangle.add_area(Triangle(1, 12, 13))


def test_add_area_square(default_circle, default_rectangle, default_square, default_triangle):
    # sum with correct classes
    assert default_square.add_area(default_circle) == 414.1592653589793
    assert default_square.add_area(default_rectangle) == 300
    assert default_square.add_area(default_square) == 200
    assert default_square.add_area(default_triangle) == 151

    # sum with other class
    with pytest.raises(ValueError):
        default_square.add_area(WrongClass)
    # sum with err target class
    with pytest.raises(TypeError):
        default_square.add_area(Triangle(1, 12, 13))


def test_add_area_triangle(default_circle, default_rectangle, default_square, default_triangle):
    # sum with correct classes
    assert default_triangle.add_area(default_circle) == 365.1592653589793
    assert default_triangle.add_area(default_rectangle) == 251
    assert default_triangle.add_area(default_square) == 151
    assert default_triangle.add_area(default_triangle) == 102

    # sum with other class
    with pytest.raises(ValueError):
        default_triangle.add_area(WrongClass)
    # sum with err target class
    with pytest.raises(TypeError):
        default_triangle.add_area(Rectangle(10, 10))
