class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if 0 <= new_floor <= house.number_of_floors:
            for i in range(new_floor):
                print(f"Перешли на {i + 1} этаж")
        else:
            print("Такого этажа не существует")


house = House("ЖК Эльбрус", 30)
house.go_to(10)

