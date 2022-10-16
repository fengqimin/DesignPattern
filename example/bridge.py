"""
Bridge
"""
from abc import abstractmethod


# Implementor
class DrawingAPI(object):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        pass


# ConcreteImplementor 1/2
class RedCircle(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f'{self.__class__.__name__} at ({x}, {y}) radius {radius}')


# ConcreteImplementor 2/2
class GreenCircle(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f'{self.__class__.__name__} at ({x}, {y}) radius {radius}')


# Abstraction
class Shape(object):
    @abstractmethod
    def draw(self):
        pass


# Refined Abstraction
class Circle(Shape):
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    # low-level i.e. Implementation specific
    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)


def main():
    shapes = (
        Circle(1, 2, 3, RedCircle()),
        Circle(5, 7, 11, GreenCircle())
    )

    for shape in shapes:
        shape.draw()


if __name__ == '__main__':
    main()
