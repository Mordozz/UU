def custom_write(file_name: str, strings: list) -> dict:
    file = open(file_name, 'a', encoding='utf-8')
    string_number, string_position = 0, 0
    summary = dict()
    for string in strings:
        string_number = string_number + 1
        string_position = file.tell()
        file.write(string + '\n')
        summary.update({(string_number, string_position): string})
    file.close()
    return summary


def main():
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)


if __name__ == '__main__':
    main()