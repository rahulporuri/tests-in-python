from numpy import pi as PI
from textwrap import dedent

class polygon():
    """

    """

    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

class Circle(polygon):
    """

    """

    def __init__(self, radius):
        self.radius = radius
    def _calculate_area(self):
        self.area = PI*int(self.radius)**2
    def _calculate_perimeter(self):
        self.perimeter = 2*PI*int(self.radius)

class Square(polygon):
    """

    """

    def __init__(self, side_length):
        self.side_length = side_length
    def _calculate_area(self):
        self.area = 4*self.side_length**2
    def _calculate_perimeter(self):
        self.perimeter = 4*self.side_length

class Rectangle(polygon):
    """

    """

    def __init__(self, size_length, size_breadth):
        self.size_length = size_length
        self.size_breadth = size_breadth
    def _calculate_area(self):
        self.area = (self.size_length + self.size_breadth)**2
    def _calculate_perimeter(self):
        self.perimeter = 2*(self.size_length + self.size_breadth)

if __name__ == "__main__":
    polygon_dict = {'1':circle, '2':square, '3':rectangle}
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
