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

# a = [int[i] for i in input('Enter a number: ').split()]
# how_many_pairs = 0
# for i in range(len(a) - 1): # по умолчанию с нулевого индекса, поэтому 1 параметр только указан
#     for j in range(1, len(a)):
#         if a[i] == a[j]:
#             how_many_pairs +=1
# print(how_many_pairs)

# На вход программе подается три натуральных числа m,p,n:
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов.
# Программа должна выводить размер популяции в каждый день, начиная с 
# 1 и заканчивая n-м днем.

# m = float(input())
# p = float(input())
# n = int(input())
# print(1, m)
# for i in range(2, n+1):
#     k = m + (m*p)/100
#     print(i, k)
#     m = k

# Бинарный поиск (доделать)

# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         guess = list[mid]
#         if item == guess:
#             return mid
#         elif item > guess:
#             low = list[mid] + 1
#         elif item < guess:
#             high = list[mid] - 1
#     return None

# my_list = [12, 23, 34, 45, 56, 67, 78, 89, 90]
# print(binary_search(my_list, 12))

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# grades = [1, 3, 4, 2, 5, 5, 4, 2, 3]
# worst = min(grades)
# best = max(grades)
# for i in range(len(grades)):
#     if grades[i] == best:
#         grades[i] = worst
# print(grades)       


# На вход подается N чисел,
# нужно вывести наибольшее и второе наибольшее.

# n = int(input())
# big_num = -1
# second_big = -2
# for i in range(n):
#     m = int(input())
#     if m > big_num:
#         second_big = big_num
#         big_num = m
#     elif m > second_big:
#         second_big = m
# print(big_num)
# print(second_big)

# Вывести N чисел Фибоначи в соответствии с условием вывода:
# в строку через пробел: 1 1 2 3 5 8 итд.

n = int(input())
f1 = 1
f2 = 1
if n > 1:
    print(f1, f2, end=' ')
    for i in range(2, n):
        f1, f2 = f2, f1+f2
        print(f2, end=' ')
       

   








        



