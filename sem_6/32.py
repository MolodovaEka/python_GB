# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

pass
def get_indexes(array, arg1, arg2):
    indexes = list()
    for i in range(0, len(array)):
        if arg1 <= array[i] <= arg2:
            indexes.append(i)
    return indexes

from random import randint
array = array = [randint(0, 20) for element in range(15)]
print(array)
low_limit = int(input('Enter a low limit value: '))
high_limit = int(input('Enter a high limit value: '))
print(get_indexes(array, low_limit, high_limit))

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
# if min_number <= list_1[i] <= max_number:
# print(i)





