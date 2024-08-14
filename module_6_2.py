class Vehicle:
    __COLOR_VARIANTS = ['green', 'black', 'red', 'yellow']

    def __init__(self, owner: str,
                 __model: str,
                 __engin_power: int,
                 __color: str):
        self.owner = owner
        self.model = __model
        self.engin_power = __engin_power
        self.color = __color

    def get_model(self):
        return f'Модель: {self.model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.engin_power}'

    def get_color(self):
        return f'Цвет: {self.color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner: str,
                 model: str,
                 engin_power: int,
                 color: str):
        super().__init__(owner, model, engin_power, color)

    def get_passengers_count(self):
        return f'Количество пассажиров: {self.passengers}'


if __name__ == '__main__':
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'red')

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()
