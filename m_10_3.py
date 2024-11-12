import time
from random import randint
from threading import Thread, Lock


class Bank(Thread):
    lock = Lock() # типа flag
    lock_ = Lock()

    def __init__(self, balance = 0):
        super().__init__()
        self.balance = balance

    def deposit(self) -> None:
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            with self.lock_:
                num = randint(50, 100)
                self.balance += num
                print(f'deposit{i+1}: \n', f'Баланс пополнен на {num} Баланс равен: {self.balance}')
            time.sleep(0.1)

    def take(self) -> None:
        for i in range(100):
            if not self.lock.locked():
                with self.lock_:
                    num = randint(50, 100)
                    print(f'take{i+1}:')
                    print(f'Запрос на снятие: {num}')
                    if self.balance >= num:
                        self.balance -= num
                        print(f'Снято: {num} Баланс: {self.balance}')
                    else:
                        print('запрос отклонен')
                        self.lock.acquire()
            time.sleep(0.1)

bk = Bank()

thr1 = Thread(target=Bank.deposit, args=(bk,))
thr2 = Thread(target=Bank.take, args=(bk,), daemon=True)

thr1.start()
thr2.start()
thr1.join()
thr2.join()

print(f'Итоговый баланс: {bk.balance}')
