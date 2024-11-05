import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power, delay = 1.0):
        Thread.__init__(self)
        self.name = name   # str
        self.power = power # int
        self.delay = delay
        self.health = 100
        self.counter = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.health > 0:
            time.sleep(1)
            self.health -= self.power
            self.counter += 1
            print(f'{self.name} сражается {self.counter} дней, осталось {self.health} воинов')
        print(f'{self.name} одержал победу спустя {self.counter} дней')

first_knight = Knight('Sir Lancelot', 10, 0.5)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')