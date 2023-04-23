# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод
# — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве
# внедрена система автоматического сбора черники. Эта система состоит
# из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint
n = int(input('Enter a number of bushes on your blackberry patch: '))
blackberry_patch = [randint(25, 40) for element in range(n)]
print(blackberry_patch)
harvest = []
i = 0
while i < n:
    harvest.append(blackberry_patch[-1] + blackberry_patch[-2] + blackberry_patch[-3])
    blackberry_patch.insert(0, blackberry_patch[-1])
    blackberry_patch.pop()
    i+=1
print(harvest)
max_harvest = max(harvest)
print(f'The biggest number of berries per time is {max_harvest}')



        