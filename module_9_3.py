first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(a) - len(b) for a,b in zip(first, second) if len(a) != len(b)]
second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]

print(first_result)
print(second_result)
