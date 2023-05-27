# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке.

vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

def count_vowels(list):
    how_many_vowels = []
    for item in list:
        count_v = 0
        for char in item:
            if char in vowels:
                count_v += 1
        how_many_vowels.append(count_v)
    return len(set(how_many_vowels)) == 1

my_phrases = [phrase for phrase in input('Enter your rythm: ').split()]
if count_vowels(my_phrases):
    print('Парам пам-пам')
else:
    print('Пам парам')



# def rythm(poem):
#     syllables = [] # список с количеством слогов в каждой фразе
#     for phrase in poem:
#         vowels = [letter for letter in phrase if letter in 'аоиеёэыуюя'] # оставляем только гласные буквы
#         # count_vowels = sum([1 for letter in phrase if letter in 'аоиеёэыуюя'])
#         syllables.append(len(vowels)) # определяем число слогов и добавляем в список
#     if len(set(syllables)) == 1: # если все числа в списке одинаковы
#         return True
#     return False

# poem = input('Введите стихотворение ').split() 
# # poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'.split()
# if rythm(poem):
#     print('Парам пам-пам')
# else:
#     print('Пам-парам')
        
    
    
