from shape import Shape


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width
