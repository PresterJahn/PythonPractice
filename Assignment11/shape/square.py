from shape import Shape


class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def get_area(self):
        return self.side ** 2
