# Задача 22: Даны два неупорядоченных набора целых чисел (может быть,
# с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах. Пользователь вводит 2 списка.
# 1 строка - первый список через пробел. 2 строка - второй список через пробел

array1 = list(map(int, input("Enter numbers for array1 ").split()))
array2 = list(map(int, input("Enter numbers for array2").split()))
resulting_set = set(array1 + array2)
print(sorted(resulting_set))

