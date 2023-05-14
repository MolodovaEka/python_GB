# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input('Enter the starting number: '))
b = int(input('Enter the number of elements: '))
c = int(input('Enter the augmentation: ')) 

def get_progression(arg1, arg2, arg3):
    progression = list()
    for i in range(1, arg2+1):
        progression.append(arg1 + (i-1)*arg3)
    return progression

print(get_progression(a, b, c))

# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
# print(a1 + i * d)



