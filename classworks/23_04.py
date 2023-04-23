# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# a1 = int(input('Ведите размер первого массива: '))
# array1 = [int(i) for i in input('Введите числа через пробел ').split()]
# a2 = int(input('Ведите размер первого массива: '))
# array2 = [int(i) for i in input('Введите числа через пробел ').split()]

# array3 = [i for i in array1 if not (i in array2)]
# print(array3)

# def my_comparison(arr1, arr2):
#     arr3 = []
#     for i in range(len(arr1)):
#         if arr1[i] not in arr2:
#             arr3.append(arr1[i])
#     return arr3

# arr1 = input('arr1: ').split()
# arr2 = input('arr2: ').split()
# arr3 = my_comparison(arr1, arr2)

# print('Первый массив: ', *arr1)
# print('Второй массив: ', *arr2)
# print('Элементов, которых нет во втором массиве: ', *arr3)

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# from random import randint
# n = int(input('Enter a number to set the length of your array '))
# array = [randint(0, 10) for element in range(n)]

# def find_neighbors_of_number(number, array):
#     count_of_neighbors = 0
#     for i in range(1,len(array)-1):
#         if (array[i-1]<number) and (array[i+1]<number):
#             count_of_neighbors = count_of_neighbors+1
#     return count_of_neighbors  

# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

a = [int[i] for i in input('Enter a number: ').split()]
how_many_pairs = 0
for i in range(len(a) - 1): # по умолчанию с нулевого индекса, поэтому 1 параметр только указан
    for j in range(1, len(a)):
        if a[i] == a[j]:
            how_many_pairs +=1
print(how_many_pairs)

