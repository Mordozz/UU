import math


class Figure:
    sides_count = 0

    def __init__(self, color: list, *sides):
        if len(color) != 3 or not self.__is_valid_color(color):
            raise ValueError("Некорректный формат палитры")
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = True

    def get_sides(self) -> list:
        return self.__sides

    def set_sides(self, *new_sides: int) -> None:
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_color(self) -> list:
        return self.__color

    def set_color(self, r: int, g: int, b: int) -> None:
        if self.__is_valid_color([r, g, b]):
            self.__color = [r, g, b]

    def __is_valid_color(self, rgb: list) -> bool:
        if len(rgb) != 3:
            return False
        for color in rgb:
            if not isinstance(color, int) or color < 0 or color > 255:
                return False
        return True

    def __is_valid_sides(self, *sides: int) -> bool:
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def __len__(self) -> int:
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: list, *sides):
        if len(sides) != 1:
            sides = [1]
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self) -> float:
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self) -> float:
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: list, *sides):
        if len(sides) != 3:
            sides = [1, 1, 1]
        super().__init__(color, *sides)

    def get_square(self) -> float:
        sides = self.get_sides()
        s = sum(sides) / 2
        return math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list, *sides):
        if len(sides) != 1:
            sides = [1] * 12
        else:
            sides = sides * 12
        super().__init__(color, *sides)

    def get_volume(self) -> float:
        side_length = self.get_sides()[0]
        return side_length ** 3

def main():
    circle1 = Circle([200, 200, 100], 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())


if __name__ == '__main__':
    main()

