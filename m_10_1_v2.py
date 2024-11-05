import threading
import time

def write_word(word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1} \n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}.')

count_list = [10,30,20,50]
name_list_1 = ['example1.txt', 'example2.txt', 'example3.txt', 'example4.txt']

#------------------------------------------------------ работа с функциями
start_functions = time.time()
for i in range(len(count_list)):
    write_word(count_list[i], name_list_1[i])
end_function = time.time()
#------------------------------------------------------  

print(f'Разница начала и конца работы функций: {int(end_function - start_functions)} c')

def write_word_stream(word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1} \n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}.')
    print(threading.current_thread())

name_list_2 = ['example5.txt', 'example6.txt', 'example7.txt', 'example8.txt']

#------------------------------------------------------ работа с потоками
start_stream = time.time()

stream_1 = threading.Thread(target=write_word_stream, args=(10, name_list_2[0])) # === создаем потоки по объектам
stream_2 = threading.Thread(target=write_word_stream, args=(30, name_list_2[1]))
stream_3 = threading.Thread(target=write_word_stream, args=(20, name_list_2[2]))
stream_4 = threading.Thread(target=write_word_stream, args=(50, name_list_2[3]))


stream_1.start() # === запускаем работу потоков
stream_2.start()
stream_3.start()
stream_4.start()

print(threading.enumerate()) # список потоков в работе

stream_1.join() # === останавливаем работу потоков
stream_2.join()
stream_3.join()
stream_4.join()

# for i in range(len(count_list)):
#     stream = threading.Thread(target=write_word_stream, args=(count_list[i],name_list_2[i]))
#     stream.start()
#     stream.join()
end_stream = time.time()
#------------------------------------------------------

print(f'Разница начала и конца работы потоков: {int(end_stream - start_stream)} c')
print(threading.enumerate()) # после остановки дополнительных потоков в списке текущих потоков остается только основной
