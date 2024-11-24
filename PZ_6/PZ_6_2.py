# Дан список размера N. Найти минимальный из его локальных максимумов
# (локальный минимум — это элемент, который меньше любого из своих соседей).

import random

numbers = []
local_maxima = []

n = input("Введите размер списка: ")

# Обработка исключений
while True:
    try:
        n = int(n)
        if n > 1:  # Нужно, чтобы было хотя бы 3 элемента для поиска локальных максимумов
            break
        else:
            print("Размер списка должен быть больше 1.")
            n = input("Введите размер списка: ")
    except ValueError:
        print("Вы неправильно ввели целое число!")
        n = input("Введите размер списка: ")

# Создаем список чисел
for z in range(n):
    numbers += [random.randint(1, 100)]

# Проходимся по элементам списка (исключая первый и последний)
for i in range(1, n - 1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        local_maxima.append(numbers[i])

# Находим минимальный из локальных максимумов и записываем его в отдельную переменную
if local_maxima:
    min_local_maximum = min(local_maxima)
else:
    min_local_maximum = "Минимального локального максимума нет"

# Вывод результатов
print("Список чисел:", numbers)
print("Локальные максимумы:", local_maxima)
print("Минимальный из локальных максимумов:", min_local_maximum)
