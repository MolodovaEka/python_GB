# Задача 22: Даны два неупорядоченных набора целых чисел (может быть,
# с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах. Пользователь вводит 2 списка.
# 1 строка - первый список через пробел. 2 строка - второй список через пробел

array1 = list(map(int, input("Enter numbers for array1 ").split()))
array2 = list(map(int, input("Enter numbers for array2").split()))
resulting_set = set(array1 + array2)
print(sorted(resulting_set))

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
# set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
# set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
# print(i, end=' ')
