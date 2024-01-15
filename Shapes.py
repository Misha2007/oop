"""Shapes."""
from abc import ABC, abstractmethod


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Shape constructor."""
        self.color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.color

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Circle constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        self.color = color
        self.radius = radius

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self.radius}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        import math
        return self.radius**2 * math.pi


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Square constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        self.side = side
        self.color = color

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.side}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self.side ** 2


class Rectangle(Shape):
    """."""

    def __init__(self, color: str, length: float, width: float):
        """."""
        self.color = color
        self.length = length
        self.width = width

    def __repr__(self) -> str:
        """."""
        return f"Rectangle (l: {self.length}, w: {self.width}, color: {self.color})"

    def get_area(self) -> float:
        """."""
        return self.length * self.width


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Paint constructor."""
        self.shapes = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.shapes.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.shapes

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        area = 0
        for i in self.shapes:
            area += i.get_area()
        return area

    def get_circles(self) -> list:
        """Return only circles."""
        list_ci = []
        for i in self.shapes:
            if type(i) is Circle:
                list_ci.append(i)
        return list_ci

    def get_squares(self) -> list:
        """Return only squares."""
        list_sq = []
        for i in self.shapes:
            if type(i) is Square:
                list_sq.append(i)
        return list_sq

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        list_re = []
        for i in self.shapes:
            if type(i) is Rectangle:
                list_re.append(i)
        return list_re


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    paint.add_shape(circle)
    paint.add_shape(square)
    print(paint.calculate_total_area())
    print(paint.get_circles())
