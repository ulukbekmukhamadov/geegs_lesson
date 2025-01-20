class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self._side_length = side_length

    def calculate_area(self):
        return self._side_length

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self._side_length}{Figure.unit}, area: {area}{Figure.unit}.")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self._length = length
        self._width = width

    def calculate_area(self):
        return self._length * self._width
    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self._length}{Figure.unit}, width: {self._width}{Figure.unit}, area: {area}{Figure.unit}.")

figures = [
    Square(5),
    Square(7),
    Rectangle(5, 8),
    Rectangle(6, 4),
    Rectangle(10, 2)
]

for figure in figures:
    figure.info()