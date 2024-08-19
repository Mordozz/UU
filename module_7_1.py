class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self) -> str:
        try:
            with open(self.__file_name, 'r') as file:
                storage = file.read()
            return storage
        # except Exception as e:
        # print("Файл не найден")
        except FileNotFoundError:
            return ""

    def add(self, *products: Product) -> None:
        current_products = self.get_products().splitlines()

        # print(f"{type(current_products)}\n {current_products}")

        for product in products:
            product_str = str(product)
            if product_str in current_products:
                print(f"Продукт {product_str} уже есть в магазине")
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(product_str + '\n')
                print(f"Продукт {product_str} добавлен в магазин")


def main():
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)
    print(s1.get_products())

    s1.add(p1, p2, p3)
    print(s1.get_products())


if __name__ == "__main__":
    main()
