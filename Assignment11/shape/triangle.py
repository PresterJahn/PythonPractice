from shape import Shape


class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def get_area(self):
        return self.base * self.height / 2
