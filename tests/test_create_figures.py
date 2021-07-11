import pytest
from src import *


def test_create_triangle(default_triangle):
    # create triangle with correct args
    assert default_triangle.area == 51
    assert default_triangle.perimeter == 33

    # create triangle with incorrect symbol
    with pytest.raises(TypeError):
        Triangle("first_arg", 11, 12)

    # create triangle with incorrect sides
    assert Triangle(1, 2, 13).area is None
    with pytest.raises(ValueError):
        Triangle(-10, -11, -12)


def test_create_circle(default_circle):
    # create circle with correct args
    assert default_circle.area == 314.1592653589793
    assert default_circle.perimeter == 62.83185307179586

    # create circle with incorrect symbol
    with pytest.raises(TypeError):
        Circle("first_arg")

    # create circle with zero or negative side
    with pytest.raises(ValueError):
        Circle(0)
    with pytest.raises(ValueError):
        Circle(-20)


def test_create_rectangle(default_rectangle):
    # create rectangle with correct args
    assert default_rectangle.area == 200
    assert default_rectangle.perimeter == 60

    # create rectangle with incorrect symbol
    with pytest.raises(TypeError):
        Rectangle("first_arg", 20)

    # create rectangle with same sides
    assert Rectangle(10, 10).area is None

    # create Rectangle with zero or negative side
    with pytest.raises(ValueError):
        Rectangle(-10, 20)
    with pytest.raises(ValueError):
        Rectangle(0, 20)


def test_create_square(default_square):
    # create square with correct args
    assert default_square.area == 100
    assert default_square.perimeter == 40

    # create square with incorrect symbol
    with pytest.raises(TypeError):
        Square("first_arg")

    # create Rectangle with zero or negative side
    with pytest.raises(ValueError):
        Square(-10)
    with pytest.raises(ValueError):
        Square(0)
