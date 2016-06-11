from numpy import pi as PI
from textwrap import dedent

class polygon():
    """ defines the prototype class for all other specific
    polygon shapes. defines the private methods _calculate_area
    and _calculate_perimeter that are defined according to the
    polygon they are defined on.

    """

    def _calculate_area(self):
        pass
    def _calculate_perimeter(self):
        pass

class Circle(polygon):
    """ defines the necessary details to define a circle
    the radius is passed to the class when it is being
    instantiated.

    """

    def __init__(self, radius):
        self.radius = int(radius)
    def _calculate_area(self):
        self.area = PI*(self.radius)**2
    def _calculate_perimeter(self):
        self.perimeter = 2*PI*self.radius

class Square(polygon):
    """ defines the necessary details to define a square.
    the side_length is passed to the class when it is being
    instantiated.

    """

    def __init__(self, side_length):
        self.side_length = int(side_length)
    def _calculate_area(self):
        self.area = 4*self.side_length**2
    def _calculate_perimeter(self):
        self.perimeter = 4*self.side_length

class Rectangle(polygon):
    """ defines the necessary details to define a rectangle.
    the length and width of the rectangle are passed to the
    class when it is being instantiated.

    """

    def __init__(self, size_length, size_breadth):
        self.size_length = int(size_length)
        self.size_breadth = int(size_breadth)
    def _calculate_area(self):
        self.area = (self.size_length + self.size_breadth)**2
    def _calculate_perimeter(self):
        self.perimeter = 2*(self.size_length + self.size_breadth)


if __name__ == "__main__":
    polygon_dict = {'1':Circle, '2':Square, '3':Rectangle}
    message = ("Choose the polygon for which you would"
              "like to calculate area and perimeter:\n"
              "1 for circle\n"
              "2 for square\n"
              "3 for rectangle\n"
    )
    user_choice_polygon_type = raw_input(dedent(message))
    if user_choice_polygon_type == '1':
        radius = raw_input("Provide the radius of the circle:\n")
        circle = polygon_dict[user_choice_polygon_type](radius)
        circle._calculate_area()
        circle._calculate_perimeter()
        print("the area of the circle is : ", circle.area,
              "the perimeter of the circle is : ", circle.perimeter
        )
    elif user_choice_polygon_type == '2':
        side_length = raw_input("Provide the length of the square's side\n")
        square= polygon_dict[user_choice_polygon_type](side_length)
        square._calculate_area()
        square._calculate_perimeter()
        print("the area of the square is : ", square.area,
              "the perimeter of the square is : ", square.perimeter
        )
    elif user_choice_polygon_type == '3':
        size_length = raw_input("Provide the length of the rectangle:\n")
        size_breadth = raw_input("Provide the breadth of the rectangle:\n")
        rectangle= polygon_dict[user_choice_polygon_type](size_length, size_breadth)
        rectangle._calculate_area()
        rectangle._calculate_perimeter()
        print("the area of the rectangle is : ", rectangle.area,
              "the perimeter of the rectangle is : ", rectangle.perimeter
        )
