class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"ЖК: {self.name}"

    def go_to(self, new_floor: int):
        if 0 <= new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(f"Перешли на {i + 1} этаж")
        else:
            print("Такого этажа не существует")

house = House('ЖК Эльбрус', 30)
house.go_to(10)
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
