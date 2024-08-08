class House:

    house_history = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        House.house_history.append(args[0])
        return instance

    def __del__(self):
        print(f'{self.name} сснесён, но он останется в истории')
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"ЖК: {self.name}, Этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __add__(self, other):
        if isinstance(other, House):
            return House(self.name, self.number_of_floors + other.number_of_floors)
        elif isinstance(other, int):
            return House(self.name, self.number_of_floors + other)
        return NotImplemented

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            new_floors = self.number_of_floors - other
        else:
            return f"Нельзя вычесть {other} этажей из {self.name}"
        return new_floors


    def go_to(self, new_floor: int):
        if 0 <= new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(f"Перешли на {i + 1} этаж")
        else:
            print("Такого этажа не существует")

h1 = House('ЖК Эльбрус', 10)
print(House.house_history)
h2 = House('ЖК Акация', 20)
print(House.house_history)
h3 = House('ЖК Матрёшки', 20)
print(House.house_history)

# Удаление объектов
del h2
del h3

print(House.house_history)