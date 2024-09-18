from threading import Thread
from time import sleep, time

def write_words(word_count: int, file_name: str):
    with open(file_name, 'a') as f:
        for i in range(word_count):
            f.write(f"Какое-то слово № {i + 1}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}\n")


start_time = time()
write_words(10, 'example1.txt')
write_words(20, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time()
print(f"Время выполнения {end_time - start_time:.2f} секунд")


thread_start_time = time()
threads = []

threads.append(Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(Thread(target=write_words, args=(20, 'example6.txt')))
threads.append(Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(Thread(target=write_words, args=(100, 'example8.txt')))

for thread in threads:
    thread.start()


for thread in threads:
    thread.join()

thread_end_time = time()
print(f"Время выполнения с использованием потоков {thread_end_time - thread_start_time:.2f} секунд")
