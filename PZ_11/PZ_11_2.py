# Из предложенного текстового файла (text18-7.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который
# поместить текст в стихотворной форме предварительно
# поставив последнюю строку между второй и третьей.

import chardet


with open('text18-7.txt', 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']

n = 0

with open('text18-7.txt', 'r', encoding=encoding) as file:
    a = file.read()
    print(a)
    for line in file:
        for char in line:
            if char.islower():
                n += 1

print(f'Количество букв в нижнем регистре : {n}')
