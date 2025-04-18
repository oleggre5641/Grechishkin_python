# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Среднее арифметическое элементов:
# Положительные четные элементы:
# Сумма положительных четных элементов:
# Среднее арифметическое положительных четных элементов:

spisok = ["12", "52", "91", "-13", "95", "-1", "62"]

with open("text_file.txt", "w") as file:
    for el in spisok:
        file.writelines(f"{el}\n")

with open("text_param.txt", "w+") as file:
    new_spisok = []
    polozh_spisok = []
    my_text_file = open("text_file.txt", "r")
    for line in my_text_file:
        new_spisok.append(int(line))

    file.writelines(f"Исходные данные: {', '.join(map(str, new_spisok))}\n")
    file.writelines(f"Количество элементов: {len(new_spisok)}\n")
    file.writelines(f"Среднее арифметическое элементов: {sum(new_spisok) // len(new_spisok)}\n")
    for el in new_spisok:
        if el > 0 and el % 2 == 0:
            polozh_spisok.append(el)
    file.writelines(f"Положительные четные элементы: {', '.join(map(str, polozh_spisok)) }\n")
    file.writelines(f"Сумма положительных четных элементов: {sum(polozh_spisok)}\n")
    file.writelines(f"Среднее арифметическое положительных четных элементов: {sum(polozh_spisok) // len(polozh_spisok)}\n")

print(spisok)
print(new_spisok)
