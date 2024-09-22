from threading import Lock, Thread
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            self.lock.acquire()
            try:
                self.balance += amount
                print(f'Пополнение: {amount}. Баланс: {self.balance}\n')
            finally:
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}\n')
            self.lock.acquire()
            try:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Снятие: {amount}. Баланс: {self.balance}\n')
                else:
                    print('Запрос отклонён, недостаточно средств\n')
            finally:

                self.lock.release()
            time.sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')