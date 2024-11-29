import time
from multiprocessing import Pool
from threading import Thread


def read_info(name):
    with open(name, 'r', encoding='utf-8') as file:
        all_data = [line for line in file]
        print(all_data[-1])

def time_thread()->None:
    start = time.time()
    for i in range(1,5):
        print(i)
        read_info(f'file {i}.txt')
    finish = time.time()
    print('line:', round(finish-start,2))


def time_multiprocess()->None:
    start1 = time.time()
    values = [f'file {i}.txt' for i in range(1,5)]
    with Pool(4) as pool:
        pool.map(read_info, values)
    finish1 = time.time()
    print('multiprocess: ', round(finish1 - start1,2))




if __name__ == '__main__':
    time_multiprocess()
    
    thread = Thread(time_thread())
    thread.start()
    thread.join()






