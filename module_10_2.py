from threading import Thread
import time

class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        days = 0
        while enemies > 0:
            days += 1
            time.sleep(1)
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f"{self.name}, сражается {days} день(дня)..., осталось {enemies} воинов.")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

knight_1 = Knight('Sir Lancelot', 10)
knight_2 = Knight('Sir Galahad', 20)

knight_1.start()
knight_2.start()

knight_1.join()
knight_2.join()

print("Все битвы закончились!")
