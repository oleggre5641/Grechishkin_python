# В двумерном списке элементы строки N
# (N задать с клавиатуры) увеличить на 3.

dv_spisok = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходный двумерный список:")
for m in dv_spisok:
    print(m)

n = int(input("Введите номер строки N (от 0 до 2): "))

if 0 <= n < len(dv_spisok):
    dv_spisok[n] = [x + 3 for x in dv_spisok[n]]
else:
    print(f"Строка с номером {dv_spisok} не существует")

print(f"Двумерный список после увеличения элементов строки {n} на 3 : ")

for a in dv_spisok:
    print(a)
