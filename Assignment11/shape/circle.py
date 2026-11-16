import math
from shape import Shape


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2
