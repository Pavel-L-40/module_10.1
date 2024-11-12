from random import randint
from threading import Thread, Lock

lock = Lock()

class Bank(Thread):
    flag = True
    def __init__(self, name, balance = 0, *args, ** kwargs):
        super().__init__()
        self.name = name
        self.balance = balance


    def first(self):
        for i in range(100):
            if self.balance > 500 and self.flag:
                self.flag = False
            if self.flag:
                with lock:
                    self.deposit()
            else:
                with lock:
                    self.take()
            print(self.balance)

    def deposit(self):
        num = randint(50, 100)
        self.balance += num
    def take(self):
        num = randint(50, 100)
        if self.balance >= num:
            self.balance -= num
        else:
            self.flag = True

bk = Bank('bk')
th1 = Thread(target=Bank.first, args=(bk, ))
th1.start()