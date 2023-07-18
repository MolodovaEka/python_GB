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
#         mid = (low + high)//2
#         guess = list[mid]
#         if item == guess:
#             return mid
#         elif item > guess:
#             low = list[mid] + 1
#         elif item < guess:
#             high = list[mid] - 1
#     return None

# my_list = [12, 23, 34, 45, 56, 67, 78, 89, 90]
# binary_search(my_list, 12)

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


# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит натуральное число из отрезка [a;b]
# с максимальной суммой делителей.

# a = int(input())
# b = int(input())
# total_divs = 0
# max_divs = 0
# the_number = 0

# for i in range(a, b + 1):
#     for j in range(1, b + 1):
#         if i % j == 0:
#             total_divs += j
#     if total_divs >= max_divs:
#         if i > the_number:
#             max_divs = total_divs
#             the_number = i
#     total_divs = 0
# print(the_number, max_divs, sep=' ')

# На вход программе подается натуральное число n. Напишите программу,
# выводящую графическое изображение делимости чисел от 1 до n включительно.
# В каждой строке надо напечатать очередное число и столько символов «+»,
# сколько делителей у этого числа.

# n = int(input())
# divs = 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             divs +=1
#     print(i, "+" * divs)
#     divs = 0

# На вход программе подается натуральное число n.
# Напишите программу, которая находит цифровой корень данного числа.
# Цифровой корень числа n получается следующим образом:
# если сложить все цифры этого числа, затем все цифры найденной суммы
# и повторять этот процесс до тех пор, пока в результате не будет получено
# однозначное число (цифра), которое и называется цифровым корнем изначального числа.

# n = int(input())
# raw_root = 0
# digital_root = 0
# while n > 0:
#     raw_root += n % 10
#     n = n // 10
# while raw_root > 0:
#     digital_root += raw_root % 10
#     raw_root = raw_root // 10
# print(digital_root)

# n = int(input())
# while n > 9:
#     n = n % 10 + n // 10
# print(n)

# Дано натуральное число n. Напишите программу, которая выводит значение суммы 
# 1!+2!+3!+…+n!.

# n = int(input())
# fact = 1
# total = 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         fact *= j
#     total = total + fact
#     fact = 1
# print(total)

# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит все простые числа от a до b включительно.

# a = int(input())
# b = int(input())
# flag = True
# if a == 1:
#     a = 2
# for i in range(a, b + 1):
#     for j in range(2, i):
#         if i % j == 0:
#             flag = False
#             break
#     if flag == True:
#         print(i)
#     flag = True

# n = int(input())
# print(19*'*')
# for _ in range(n-2):
#     print('*', 17*' ', '*', sep='')
# print(19*'*')

# n = int(input())
# while n > 999:
#     n //= 10
# third = n % 10
# print(third)

# n = int(input())
# count3 = 0
# last = n % 10
# count_last = 0
# count_even = 0
# total_big = 0
# product_biggest = 1
# count5_0 = 0
# while n > 0:
#     last_d = n % 10
#     if last_d == last:
#         count_last += 1
#     if last_d == 3:
#         count3 += 1
#     if last_d % 2 == 0:
#         count_even += 1
#     if last_d > 5:
#         total_big += last_d
#     if last_d > 7:
#         product_biggest *= last_d
#     if last_d == 0 or last_d == 5:
#         count5_0 += 1
#     n = n // 10
# print(count3)
# print(count_last)
# print(count_even)
# print(total_big)
# print(product_biggest)
# print(count5_0) 

# сумма двух кубов двумя разными способами

#  for i in range (1, 33):
#      for j in range(2, 32):
#          for k in range(3, 31):
#              for q in range(4, 30):
#                      if i ** 3 + j ** 3 == k ** 3 + q ** 3 and i != j and j != k and k != q:
#     print(i ** 3 + j ** 3 == k ** 3 + q ** 3)
# s = input()
# for c in s:
#     if c in "0123456789":
#         print('Цифра')
#         break
# else:
#     print('Цифр нет')


# s = input()
# count_vowels = 0
# count_consonants = 0
# for c in s:
#     if c in 'ауоыиэяюёе':
#         count_vowels += 1
#     elif c in 'бвгджзйклмнпрстфхцчшщ':
#         count_consonants += 1
# print(f'Количество гласных букв равно {count_vowels}')
# print(f'Количество согласных букв равно {count_consonants}') 

# Десятичное число в двоичное:

# n = int(input())
# s = ''
# while n > 0:
#     a = n % 2
#     s = str(a) + s
#     n //= 2
# print(s)

# s = 'abcdefg'
# print(s[::-3])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# s1 = s[:13]
# print(s1)

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# s1 = s[-9:]
# print(s1)

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# s1 = s[::-1]
# print()
# Палиндром или нет?
# s = input()
# m = len(s) // 2
# s1 = s[:m]
# s2 = s[-1:-m-1:-1]
# if s1 == s2:
#     print('YES')
# else:
#     print('NO')

# s = input()
# s1 = s[::-1]
# if s1 == s:
#     print('YES')
# else:
#     print('NO')

# Вывести для поданой строки:
# общее количество символов в строке;
# исходную строку, повторенную 3 раза;
# первый символ строки;
# первые три символа строки;
# последние три символа строки;
# строку в обратном порядке;
# строку с удаленным первым и последним символом.

# s = input()
# print(len(s))
# print(s*3)
# print(s[0])
# print(s[0:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:-1])

# Вывести для поданой строки:
# третий символ этой строки;
# предпоследний символ этой строки;
# первые пять символов этой строки;
# всю строку, кроме последних двух символов;
# все символы с четными индексами;
# все символы с нечетными индексами;
# все символы в обратном порядке;
# все символы строки через один в обратном порядке, начиная с последнего.

# s = input()
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])

# На вход программе подается строка текста. Напишите программу,
# которая разрежет ее на две равные части, переставит их местами
# и выведет на экран.

# s = input()
# l = len(s)//2
# s1 = s[-l:]
# s2 = s1 + s
# s3 = s2[:-l]
# print(s3)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Дан список с затратами на рекламу. Но в данных есть ошибки,
# некоторые затраты имеют отрицательную величину. Удалите
# такие значения из списка и посчитайте суммарные затраты

# def total_costs(list):
#     positives = [i for i in list if i > 0]
#     total = sum(positives)
#     return(total)

# costs = [-90,-89,-78,-56, 1, -90, 2, 3, 5]
# print(total_costs(costs))


# На складе лежат разные фрукты в разном количестве.
# Нужно написать функцию, которая на вход принимает любое
# количество названий фруктов и их количество, а возвращает
# общее количество фруктов на складе

# # Получаем 2 списка (ради повторения пройденного):
# fruits = ['бананы', 'яблоки', 'персики', 'груши', 'лимоны', 'авокадо', 'манго']
# pieces = [12, 23, 27, 19, 21, 24, 14]

# Создаем из двух списков словарь:
# def create_dict(keys: list[str], values: list[int]):
#     my_warehouse = {}
#     for i in range(len(keys)):
#         my_warehouse[keys[i]] = values[i]
#     return my_warehouse

# Проверка, что все получилось:
# my_fruits = create_dict(fruits, pieces)
# print(my_fruits)

# # Добавляем еще два словаря:
# add_1 = {'яблоки': 50, 'груши': 90, 'ананасы': 15}
# add_2 = {'яблоки': 30, 'бананы': 30, 'манго': 30}

# # Пишем функцию, которая будет к содержимому склада добавлять фрукты:
# from collections import Counter

# def merge_dicts(*dictionaries):
#     result = Counter()
#     for dictionary in dictionaries:
#         result.update(dictionary)
#     return dict(result)

# # Проверяем, всё ли добавилось:
# warehouse = merge_dicts(my_fruits, add_1, add_2)
# print(warehouse)

# # Считаем общее количество фруктов:
# total_fruits = sum(list(warehouse.values()))
# print(total_fruits)

# Домашнее задание 4: Даны два списка, "Дата покупки" и "Суммы покупок по датам".
# 4.1 Найдите, какая выручка у компании в ноябре
# 4.2 Найдите выручку компании в зависимости от месяца

dates = ['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', '2021-09-30', '2021-12-22', '2021-11-29', '2021-12-24', '2021-11-26', '2021-10-27', '2021-12-18', '2021-11-09', '2021-11-23', '2021-09-27',
'2021-10-02', '2021-12-27', '2021-09-20', '2021-12-13', '2021-11-01', '2021-11-09', '2021-12-06', '2021-12-08', '2021-10-09', '2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13', '2021-10-26', '2021-12-09']
amount = [1270, 8413, 9028, 3703, 5739, 4095, 295, 4944, 5723, 3701, 4471, 651, 7037, 4274, 6275, 4988, 6930, 2971, 6592, 2004, 2822, 519, 3406, 2732, 5015, 2008, 316, 6333, 5700, 2887]

def create_dict(keys: list[str], values: list[int]):
    my_amount = {}
    for i in range(len(keys)):
        if keys[i] not in my_amount:
            my_amount[keys[i]] = values[i]
        else:
            my_amount[keys[i]] += values[i]
    return my_amount

amount_yearly = create_dict(dates, amount)
print(amount_yearly)

def november_sum(d: list, a: list):
    res = 0
    for i in range(len(d)):
        if '-11-' in d[i]:
            res += a[i]
    return res

def month_amount(d: list[str], a: list[int]):
    my_amount = {}
    for i in range(len(d)):
        month = d[i][5:7]
        if month not in my_amount:
            my_amount[month] = a[i]
        else:
            my_amount[month] += a[i]
    return my_amount  

print('Выручка в ноябре равна', november_sum(dates, amount)) 
print('Выручка по месяцам равна', month_amount(dates, amount))

# def monthly_amount(d: dict(), month: str):
#     monthly_d = {}
#     for key in dict.keys():
#         monthly_d = {key: value for (key, value) in dict.items() if month in key}
#     return monthly_d

# # Для проверки:
# november_amount = monthly_amount(amount_yearly, '-11-')
# print(november_amount)

# # Выручка за месяц:
# def monthly_total(dict):
#     x = sum(list(dict.values()))
#     return x

# print(monthly_total(november_amount))

