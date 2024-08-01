#1
def print_params(a=1, b='строка', c=True):
    print(f"a = {a}, b = {b}, c = {c}")
print_params()
print_params(10)
print_params(b=25)
print_params(c=[1, 2, 3])

#2
def print_params(a=1, b='строка', c=True):
    print(f"a = {a}, b = {b}, c = {c}")
values_list = [10, 'новая строка', False]
values_dict = {'a': 5, 'b': 'другая строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)

#3
def print_params(a=1, b='строка', c=True):
    print(f"a = {a}, b = {b}, c = {c}")
values_list_2 = [54.32, 'Строка']
additional_param = 42
print_params(*values_list_2, additional_param)
