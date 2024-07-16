my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
existing_value = my_dict.get('Masha', None)
print(f"Existing value: {existing_value}")
not_existing_value = my_dict.get('Ivan', None)
print(f"Not existing value: {not_existing_value}")
deleted_value = my_dict.pop('Egor', None)
print(f"Deleted value: {deleted_value}")
my_dict.update({'Kamila': 1981, 'Artem': 1915})
print(f"Modified dictionary: {my_dict}")
my_set = {1, 'Яблоко', 42.314}
my_set.update({13, (5, 6, 1.6)})
print(f"Modified set: {my_set}")