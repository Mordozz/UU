def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(3)
print_params(3, 'Sybil')
print_params(True, 'другой текст', False)
print_params(b=25, c=[1, 2, 3])

values_list = [2, "тройка", False]
values_dict = {'a': 3.14, 'b': 'Draw', 'c': None}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
