import queue
import threading
import random
import time



class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        rand_num = random.randint(3, 10)
        time.sleep(rand_num)

class Cafe:
    def __init__(self, *args):
        self.tables = args
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        counter = len(self.tables)
        for num in range(len(guests)):
            if counter:
                self.tables[num].guest = guests[num]
                self.tables[num].guest.start()
                print(f'{self.tables[num].guest.name} сел за стол {self.tables[num].number}')
                counter -= 1
            else:
                self.queue.put(guests[num])
                print(f'{guests[num].name} в очереди')

    def discuss_guests(self):  # обслужить гостей
        reserv_table = 0
        for i in range(len(self.tables)):
            if self.tables[i] != None:
                reserv_table += 1
        while not self.queue.empty() or reserv_table:
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} за столом {table.number} покушал и ушел')
                    print(f'стол номер {table.number} свободен')
                    table.guest = None
                    reserv_table -= 1
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел из очереди и сел за стол номер {table.number}')
                        table.guest.start()
                        reserv_table += 1
                time.sleep(1)



tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya',
                'Arman','Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)

cafe.discuss_guests()