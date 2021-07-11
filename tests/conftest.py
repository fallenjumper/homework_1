import pytest
from src import *


@pytest.fixture
def default_circle():
    circle = Circle(10)
    yield circle
    del circle


@pytest.fixture
def default_rectangle():
    rectangle = Rectangle(10, 20)
    yield rectangle
    del rectangle


@pytest.fixture
def default_square():
    square = Square(10)
    yield square
    del square


@pytest.fixture
def default_triangle():
    triangle = Triangle(10, 11, 12)
    yield triangle
    del triangle
