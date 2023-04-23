# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def a_plus_b(arg1, arg2):
    if arg2 == 0:
        return arg1
    elif arg2 > 0:
        return a_plus_b(arg1 + 1, arg2 - 1)
    else:
        return a_plus_b(arg1 - 1, arg2 + 1)

a = int(input('Enter number A: '))
b = int(input('Enter number B: '))
print(a_plus_b(a, b))
