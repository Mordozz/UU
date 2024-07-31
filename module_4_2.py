def test_function():
    def inner_function() -> str:
        return "Я в области видимости функции test_function"

    print(f"{inner_function()}")


test_function()
#inner_function()