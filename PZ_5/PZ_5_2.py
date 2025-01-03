# Описать функцию AddRightDigit(D, K), добавляющую к целому положительному
# числу K справа цифру D (D — входной параметр целого типа, лежащий в диапазоне
# 0-9, K — параметр целого типа, являющийся одновременно входным и выходным).
# С помощью этой функции последовательно добавить к данному числу K справа
# данные цифры D1 и D2, выводя результат каждого добавления.

def AddRightDigit(d, k):  # Создание функции
    k = k * 10 + d
    return k


k = input("Введите исходное число: ")
d1 = input("Введите первую цифру: ")
d2 = input("Введите вторую цифру: ")

while type(k) != int:  # Обработка исключений
    try:
        k = int(k)
    except ValueError:
        print("Неправильно ввели!")
        k = input("Введите целое число: ")


while type(d1) != int:  # Обработка исключений
    try:
        d1 = int(d1)
        if d1 > 9:
            raise ValueError
    except ValueError:
        print("Неправильно ввели целое число!")
        d1 = input("Введите первую цифру: ")


while type(d2) != int:  # Обработка исключений
    try:
        d2 = int(d2)
        if d2 > 9:
            raise ValueError
    except ValueError:
        print("Неправильно ввели целое число!")
        d2 = input("Введите вторую цифру: ")

print(f"Резуьтат добавления первой цифры: {AddRightDigit(d1,k)}")
print(f"Резуьтат добавления второй цифры: {AddRightDigit(d2,k)}")
