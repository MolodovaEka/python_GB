import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
print(data.head(20))
# pd.get_dummies(data)

# создаем список, где "привязываем" к категорям бинарные значение
categories = list(set(lst))
# print(categories)
category_map = {category: [1 if item == category else 0 for item in categories] for category in categories}
# print(category_map)

# создаем столбец для каждой категории и вписываем туда бинарные значения
for category in categories:
    data[f'{category}_hot'] = [1 if item == category else 0 for item in lst]

# заменяем исходный столбец
data.drop('whoAmI', axis=1, inplace=True)

print(data.head(20))