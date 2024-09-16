import threading
import random
import time
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            cash = random.randint(50, 500)
            if self.balance >= cash and self.lock.locked():
                self.lock.release()
            self.balance += cash
            print(f"Пополнение: {cash}. Баланс: {self.balance}")
            time.sleep(randint(1, 2))

    def take(self):
        for i in range(100):
            cash = random.randint(50, 500)
            print(f"Запрос на {cash}")
            if cash > self.balance:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            else:
                self.balance -= cash
                print(f"Снятие: {cash}. Баланс: {self.balance}")
                time.sleep(randint(1, 2))


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
