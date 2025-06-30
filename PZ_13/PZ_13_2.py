# В двумерном списке элементы последнего
# столбца заменить на -1.

dv_spisok = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходный двумерный список : ")
list(map(print, dv_spisok))

dv_spisok = list(map(lambda row: row[:-1] + [-1], dv_spisok))  

print("Измененный двумерный список : ")
list(map(print, dv_spisok)
     
