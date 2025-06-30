# В двумерном списке элементы строки N
# (N задать с клавиатуры) увеличить на 3.

dv_spisok = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходный двумерный список:")
list(map(print, dv_spisok))

n = int(input("Введите номер строки N (от 0 до 2): "))

dv_spisok = list(map(lambda i, row: list(map(lambda x: x + 3, row)) if i == n else row, range(len(dv_spisok)), dv_spisok)) if 0 <= n < len(dv_spisok) else dv_spisok

print(f"Двумерный список после увеличения элементов строки {n} на 3 : ")
list(map(print, dv_spisok))
