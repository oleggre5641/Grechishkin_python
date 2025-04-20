# В двумерном списке элементы последнего
# столбца заменить на -1.

dv_spisok = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходный двумерный список : ")
for m in dv_spisok:
    print(m)

for n in dv_spisok:
    n[-1] = -1

print("Измененный двумерный список : ")
for a in dv_spisok:
    print(a)
