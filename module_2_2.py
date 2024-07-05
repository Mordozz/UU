a = input("Введите числа a: ")
b = input("Введите числа b: ")
c = input("Введите числа c: ")

if a == b and b == c and a == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
