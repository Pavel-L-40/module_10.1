import threading
import time

def write_words(words_count, file_name):
    with open(file_name, 'w', encoding='utf8') as file:
        for item in range(words_count):
            file.write(f"Какое-то слово № {item + 1} \n")
            time.sleep(0.1)
    print(f'завершилась запись в файл {file_name}')

# === start func ==========================================
start_func = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_func = time.time()
# === end func ============================================
print('разница начала и конца работы функций:', int(end_func - start_func),'сек')

# start streams ====================================================================
start_streams = time.time()

stream_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
stream_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
stream_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
stream_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

stream_1.start()
stream_2.start()
stream_3.start()
stream_4.start()

stream_1.join()
stream_2.join()
stream_3.join()
stream_4.join()

end_streams = time.time()
# end streams ======================================================================
print('разница начала и конца работы потоков:', int(end_streams - start_streams),'сек')

