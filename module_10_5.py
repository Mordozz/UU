import time
from datetime import timedelta
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            data = file.readline()
            if not data:
                break
            all_data.append(data.strip())

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()

    print(f"{timedelta(seconds=end_time - start_time)} (линейный)")

    start_time_mp = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time_mp = time.time()
    print(f'{timedelta(seconds=end_time_mp - start_time_mp)} (многопроцессный)')
