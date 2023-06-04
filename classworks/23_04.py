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

# n = int(input())
# f1 = 1
# f2 = 1
# if n > 1:
#     print(f1, f2, end=' ')
#     for i in range(2, n):
#         f1, f2 = f2, f1+f2
#         print(f2, end=' ')
       

#  "Ведьмаку заплатите чеканной монетой
#  (минимальным кол-вом монет достоинством 1, 5, 10 или 25)"  

# price = int(input("цена вопроса: "))
# coins_needed = 0
# while price >= 25:
#     coins_needed += 1
#     price -= 25
# while price >= 10:
#     coins_needed += 1
#     price -= 10
# while price >= 5:
#     coins_needed += 1
#     price -= 5
# while price >= 1:
#     coins_needed = coins_needed + 1
#     price -= 1
# print(coins_needed)



# На вход подается число, выведите:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

# num = int(input('Enter a number: '))
# how_many = 1
# sum_of_dgts = 0
# last_one = num % 10
# product = 1
# while num > 10:
#     how_many += 1
#     sum_of_dgts += (num % 10)
#     product = product * (num % 10)
#     num = num // 10
# first_one = num % 10
# print(sum_of_dgts + first_one)
# print(how_many)
# print(product * first_one)
# print(float((sum_of_dgts + first_one) / how_many))
# print(first_one)
# print(first_one + last_one)


# glasnye = ["а", "о", "у", "ы", "э", "е", "ё", "и", "ю", "я"]

# def same_by(charsacteristic, objects):
#     objects = set(map(charsacteristic, objects))
#     return len(objects) == 1

# def how_many_slogov(fraze):
#     glasnye_of_fraze = [i for i in fraze if i in glasnye]
#     return len(glasnye_of_fraze)


# stih = 'пара-ра-рам рам-папам па-ра-па-да'
# if same_by(how_many_slogov, stih.split()):
#     print("Парам пам-пам")
# else:
#     print("Пам парам") 

# Если число состоит из одинаковых цифр, выведите YES, иначе выведите NO:
# num = int(input())
# last_f = num % 10
# flag = True
# while num > 0:
#     if num % 10 != last_f:
#         flag = False
#         break
#     else:
#         num = num // 10

# if flag == True:
#     print('Yes') 
# else:
#     print('No')

# Проверьте, является ли число справа налево упорядоченным по неубыванию

# num = int(input())
# flag = True
# while num > 10:
#     if num % 10 > (num // 10) % 10:
#         flag = False
#         break
#     else:
#         num = num // 10

# if flag == True:
#     print('YES')
# else:
#     print('NO')

# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20

# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')

# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# count = 0
# product = 1
# for i in range(10):
#     x = int(input())
#     if x > 0:
#         product *= x
#         count += 1
# if count > 0:
#     print(count)
#     print(product)
# else:
#     print('NO')   

# maxi = -10**6
# total = 0
# for _ in range(10):
#     x = int(input())
#     if x < 0:
#         total += x
#         if x > maxi:
#             maxi = x
# if total == 0:
#     print('NO')  
# else:
#     print(total)
#     print(maxi)   


# На обработку поступает натуральное число. Нужно написать программу,
# которая выводит на экран максимальную цифру числа, кратную 
# 3. Если в числе нет цифр, кратных  3, требуется на экран вывести «NO».

# n = int(input())
# max_digit = n % 10
# while n > 0:
#     digit = n % 10
#     if digit == 0 or digit > max_digit:
#         if digit % 3 == 0:
#             max_digit = digit
#     n = n // 10
# if max_digit >= 0 and max_digit % 3 == 0:
#     print(max_digit)
# else:
#     print('NO')

# n = int(input())
# while n > 10:
#     n //= 10
# print(n)

# n = int(input())
# product = n % 10
# while n >= 10:
#     n //= 10
#     digit = n % 10
#     product = product * digit
# print(product) 

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# n = int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print() 

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(5):
#         print(i, end=' ')
#     print()   

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i + j)
#     print() 

# n = int(input())
# for i in range(1, n // 2 + 2):
#     print('*' * i)
# for j in range(n // 2 + 1, n + 1):
#     print('*' * (n - j))


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end='')
#     print()

# Решите уравнение в натуральных числах 28n + 30k + 31m = 365.
# Примечание. Используйте вложенный цикл for. В первую очередь запишите
# решение с наименьшим значением n.

# total = 0
# for n in range(1, 13):
#     for k in range(1, 12):
#         for m in range(1, 11):
#             if n * 28 + k * 30 + m * 31 == 365:
#                 total += 1
#                 print('n =', n, 'k =', k, 'm =', m)
# print('Общее количество натуральных решений =', total)


# Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги,
# если плата за быка – 10 рублей, за корову – 5 рублей, за теленка – 0.5 рубля
# и надо купить 100 голов скота?

# for b in range(1, 10):
#     for k in range(1, 20):
#         for t in range(1, 200):
#             if b * 10 + k * 5 + t * 0.5 == 100 and b + k + t == 100:
#                 print('b =', b, 'k =', k, 't =', t)

# Дано натуральное число n. Напишите программу, которая печатает численный треугольник
# с высотой равной n, в соответствии с примером.
# n = int(input())
# counter = 1
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(counter, end=' ')
#         counter +=1
#     print()


# n = int(input())
# counter = 1
# for i in range(1, n + 1):
#     for _ in range(1, i):
#         print(counter, end='')
#         counter += 1
#     for _ in range(counter - 1, -1, -1):
#         print(counter, end='')
#         counter -= 1
#     counter = 1
#     print()


# На вход программе подается два натуральных числа a и b (a< b).
# Напишите программу, которая находит натуральное число из отрезка [a;b]
# с максимальной суммой делителей.

a = int(input())
b = int(input())
total_divs = 0
max_divs = 0
the_number = 0

for i in range(a, b + 1):
    for j in range(1, b + 1):
        if i % j == 0:
            total_divs += j
    if total_divs >= max_divs:
        if i > the_number:
            max_divs = total_divs
            the_number = i
    total_divs = 0
print(the_number, max_divs, sep=' ')

