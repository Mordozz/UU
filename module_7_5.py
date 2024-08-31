import os
import time


def walktrough_directory(directory):
    for root, dirs, files in os.walk(directory):

        # for dir in dirs:
        #     dir_path = os.path.join(root, dir)
        #     print(f"Директория {dir_path}")

        for file in files:
            file_path = os.path.join(root, file)
            file_time = os.path.getmtime(file_path)
            file_size = os.path.getsize(file_path)
            file_parent_dir_name = os.path.dirname(file_path)
            f_time = time.strftime('%d.%m.%Y %H:%m', time.localtime(file_time))

            print(
                f"Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, Время изменения: {f_time}, Родительская директория: {file_parent_dir_name}")


def main():
    directory = "."
    walktrough_directory(directory)


if __name__ == '__main__':
    main()
