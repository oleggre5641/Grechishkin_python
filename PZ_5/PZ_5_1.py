# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m.
# Суммирование оформить функцией с параметрами.
# Значения n и m программа должна запрашивать.

def SumFrom(n, m):  #Создание функции
    cur = n
    summ = 0
    while cur != m:
        summ += cur
        cur += 1
    return summ


n = input("Введите первое число: ")
m = input("Введите второе число: ")

while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите целое число: ")


while type(m) != int:  # Обработка исключений
    try:
        m = int(m)
    except ValueError:
        print("Неправильно ввели!")
        m = input("Введите целое число: ")

print(f"Сумма от первого числа до второго равна: {SumFrom(n, m)}")
