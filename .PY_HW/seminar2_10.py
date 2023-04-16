# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть

from random import randint
n = int(input("Enter a number of coins: "))
coin_type0 = 0
coin_type1 = 0
for i in range(n):
    s = randint(0,1)
    print(s)
    if s == 0:
        coin_type0 +=1
    else: coin_type1 +=1
if coin_type0 > coin_type1:
    print(f'You have to turn {coin_type1}')
else:
    print(f'You have to turn {coin_type0}')