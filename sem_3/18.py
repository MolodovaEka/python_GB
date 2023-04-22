# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint
n = int(input('Enter a number to set the length of your array '))
array = [randint(0, 100) for element in range(n)]
print(array)
x = int(input('Enter the number X '))
for i in array:
    y = x - 1
    if x - i < y:
        y = x - i
print('The closest to X number in your array is', i, '.')

