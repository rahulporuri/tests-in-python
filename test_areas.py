import unittest
from numpy import pi as PI

from polygon_areas import Circle, Square, Rectangle

class testPolygonAreas(unittest.TestCase):
    """ test the classes defined in polygon_areas.py and
    verify that the results they produce are correct.

    the individual methods defined below follow the format -
    1. manually define input to the classes
    2. calculate what we expect the output of classes to be
    3. use the classes to calculate the output and cross check

    """

    def test_circle(self):
        radius = 5
        area = PI*radius**2
        perimeter = 2*PI*radius

        circle = Circle(radius)
        circle._calculate_area()
        circle._calculate_perimeter()

        self.assertEqual(area, circle.area)
        self.assertEqual(perimeter, circle.perimeter)

    def test_square(self):
        side_length = 5
        area = 4*side_length**2
        perimeter = 4*side_length

        square = Square(side_length)
        square._calculate_area()
        square._calculate_perimeter()

        self.assertEqual(area, square.area)
        self.assertEqual(perimeter, square.perimeter)

    def test_rectangle(self):
        size_length = 3
        size_breadth = 5

        area = (size_length + size_breadth)**2
        perimeter = 2*(size_length + size_breadth)

        rectangle = Rectangle(size_length, size_breadth)
        rectangle._calculate_area()
        rectangle._calculate_perimeter()

        self.assertEqual(area, rectangle.area)
        self.assertEqual(perimeter, rectangle.perimeter)
