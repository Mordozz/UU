def calculate_structure_sum(data_):
    def summiter(item):
        summarizer = 0
        if isinstance(item, int):
            summarizer += item
        elif isinstance(item, str):
            summarizer += len(item)
        elif isinstance(item, (list, tuple, set)):
            for element in item:
                summarizer += summiter(element)
        elif isinstance(item, dict):
            for key, value in item.items():
                summarizer += len(key) + summiter(value)
        return summarizer

    total_sum = 0
    for element in data_:
        total_sum += summiter(element)

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
