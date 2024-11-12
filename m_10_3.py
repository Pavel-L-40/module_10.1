import threading
import time
from random import randint
lock_main = threading.Lock()


class Bank(threading.Thread):
    lock = threading.Lock()
    def __init__(self, balance = 0):
        super().__init__()
        self.balance = balance

    def deposit(self) -> None:
        for i in range(100):
            lock_main.acquire()
            num = randint(50, 100)
            self.balance += num
            print(f'deposit {i+1} \nпополнение: {num} текущий таланс: {self.balance}')
            lock_main.release()
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.03)

    def take(self) -> None:
        for j in range(100):
            lock_main.acquire()
            num2 = randint(50, 500)
            print(f'take {j+1}: запрос {num2} ')
            if num2 <= self.balance:
                self.balance -= num2
                print(f'снятие: {num2}, текущий баланс:{self.balance}\n')
            else:
                print('запрос отклонен\n')
                if self.lock.locked() == False:
                    self.lock.acquire()
            lock_main.release()
            time.sleep(0.03)



bank1 = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bank1,))
th2 = threading.Thread(target=Bank.take, args=(bank1,), daemon=True)

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bank1.balance}')
