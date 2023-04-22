# Задача 16: Требуется вычислить, сколько раз 
# встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint
n = int(input('Enter a number to set the length of your array '))
array = [randint(0, 10) for element in range(n)]
print(array)
x = int(input('Enter a number to look for in your array '))
how_many_times = 0
for i in array:
    if i == x:
        how_many_times += 1
print(f'The number {x} occurs in your array {how_many_times} times')


