def add_everything(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)

def main():
    print(add_everything(123.456, 'строка'))
    print(add_everything('яблоко', 4215))
    print(add_everything(123.456, 7))

if __name__ == '__main__':
    main()
