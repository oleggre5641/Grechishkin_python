# Дан целочисленный список размера 10.
# Вывести все содержащиеся в данном списке
# нечетные числа в порядке возрастания их
# индексов, а также их количество K.

import random

random_spisok = []
odd_numbers = []

# Создание и добавление целых чисел в список , с помощью random
for i in range(10):
    random_spisok += [random.randint(1, 100)]

print("Сгенерированный список: ", random_spisok)

# Добавление нечетных чисел в отдельный список
for number in random_spisok:
    if number % 2 != 0:
        odd_numbers.append(number)

# Вывод нечетных чисел и их количества
print("Нечетные числа: ", odd_numbers)
print("Количество нечетных чисел: ", len(odd_numbers))
