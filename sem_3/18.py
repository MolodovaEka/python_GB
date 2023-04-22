# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint
n = int(input('Enter a number to set the length of your array '))
array = [randint(1, 100) for element in range(n)]
print(array)
x = int(input('Enter the number X '))
a = abs(array[0] - x)
the_closest = 0
for i in range(1, len(array)):
    if abs(array[i] - x) <= a:
        a = abs(array[i] - x)
        the_closest = array[i]
print(f'The number that is the closest to X in your array is {the_closest}')



