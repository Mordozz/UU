my_dict = {"Alex": 1600,
           "Peter": 1999,
           "Olga": 2222,
           "Eugeniy": 2005
        }

print(f"Dict: {my_dict}")
print(f"Existing value: {my_dict.get('Alex')}")
print(f"Not existing value: {my_dict.get('Anton')}")
print(f"Deleted value: {my_dict.pop('Peter')}")
my_dict.update({'Svetlana': 1960, 'Semyon': 1990})
print(f"Modified dictionary: {my_dict}\n")

my_set = {1, "Яблоко", "Яблоко", 1, 3, False}
print(f"Set: {my_set}")
my_set.update((7, 8), [45.375685])
print(f"Modified set: {my_set}")
