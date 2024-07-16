immutable_var = 1, 2, 3
print(immutable_var)
#immutable_var[0] = 10
print(immutable_var)
print('Кортеж не поддерживает обращение по элементам, кортеж больше подходит для хранения неизменяемого списка')
mutable_list = [[5, 6], 7]
mutable_list[0][1] = 9
print(mutable_list)
