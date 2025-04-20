# Организовать и вывести последовательность из N случайных целых чисел. Из
# исходной последовательности организовать первую последовательность, содержащую
# четные числа, и вторую – для всех остальных. Найти среднее арифметическое в полученных
# последовательностях.

import random

n = int(input("Введите количество чисел в последовательности : "))

posled = [random.randint(1, 100) for i in range(n)]

chet_numbers = [num for num in posled if num % 2 == 0]
other_numbers = [num for num in posled if num % 2 != 0]

chet_average = sum(chet_numbers) / len(chet_numbers) if chet_numbers else 0
other_average = sum(other_numbers) / len(other_numbers) if other_numbers else 0

print("Ваша исходная последовательность :", posled)
print("Среднее арифметическое четных чисел :", chet_average)
print("Среднее арифметическое остальных чисел :", other_average)
