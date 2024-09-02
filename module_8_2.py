def personal_sum(numbers: list) -> tuple[int, int]:
    result = 0
    incorrect_data = 0

    if isinstance(numbers, (list, tuple)):
        for number in numbers:
            try:
                result += number
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {number}')
        return result, incorrect_data
    else:
        raise TypeError("Передан некорректный тип данных")


def calculate_average(numbers: list) -> float:
    try:
        total_sum, incorrect_data = personal_sum(numbers)
        valid_count = len(numbers) - incorrect_data

        if valid_count == 0:
            return 0

        return total_sum / valid_count

    except ZeroDivisionError:
        return 0

    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None


def main():
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать


if __name__ == '__main__':
    main()
