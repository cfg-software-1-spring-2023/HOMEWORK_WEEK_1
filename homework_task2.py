import abc
import math


class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self):
        """Calculate perimeter"""
        return


class Polygon(Shape):
    def __init__(self, sides):
        self.sides = sides

    def calc_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__([a, b, c])
        self.a = a
        self.b = b
        self.c = c

    def calc_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area


class Quadrilateral(Polygon):
    def __init__(self, a, b, c, d):
        super().__init__([a, b, c, d])
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calc_area(self):
        s1 = (self.a + self.b + self.c + self.d) / 2
        area = math.sqrt((s1 - self.a) * (s1 - self.b) * (s1 - self.c) * (s1 - self.d))
        return area


class Square(Quadrilateral):
    def __init__(self, a):
        super().__init__(a, a, a, a)
        self.a = a


class Rectangle(Quadrilateral):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
        self.a = a
        self.b = b


triangle = Triangle(3, 4, 5)
print(f"Perimeter of triangle: {triangle.calc_perimeter()}")
print(f"Area of triangle: {triangle.calc_area()}")
import abc
import math


class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self):
        """Calculate perimeter"""
        return


class Polygon(Shape):
    def __init__(self, sides):
        self.sides = sides

    def calc_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__([a, b, c])
        self.a = a
        self.b = b
        self.c = c

    def calc_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area


class Quadrilateral(Polygon):
    def __init__(self, a, b, c, d):
        super().__init__([a, b, c, d])
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calc_area(self):
        s1 = (self.a + self.b + self.c + self.d) / 2
        area = math.sqrt((s1 - self.a) * (s1 - self.b) * (s1 - self.c) * (s1 - self.d))
        return area


class Square(Quadrilateral):
    def __init__(self, a):
        super().__init__(a, a, a, a)
        self.a = a


class Rectangle(Quadrilateral):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
        self.a = a
        self.b = b


triangle = Triangle(3, 4, 5)
print(f"Perimeter of triangle: {triangle.calc_perimeter()}")
print(f"Area of triangle: {triangle.calc_area()}")

square = Square(5)
print(f"Perimeter of square: {square.calc_perimeter()}")
print(f"Area of square: {square.calc_area()}")

rectangle = Rectangle(3, 5)
print(f"Perimeter of rectangle: {rectangle.calc_perimeter()}")
print(f"Area of rectangle: {rectangle.calc_area()}")



square = Square(5)
print(f"Perimeter of square: {square.calc_perimeter()}")
print(f"Area of square: {square.calc_area()}")

rectangle = Rectangle(3, 5)
print(f"Perimeter of rectangle: {rectangle.calc_perimeter()}")
print(f"Area of rectangle: {rectangle.calc_area()}")



