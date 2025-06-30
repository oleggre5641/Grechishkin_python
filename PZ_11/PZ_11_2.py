# Из предложенного текстового файла (text18-7.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который
# поместить текст в стихотворной форме предварительно
# поставив последнюю строку между второй и третьей.

import chardet


with open('text18-7.txt', 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']

with open('text18-7.txt', 'r', encoding=encoding) as file:
    lines = file.readlines()
    content = ''.join(lines)
    print(content)
    
    n = sum(1 for char in content if char.islower())
    print(f'Количество букв в нижнем регистре: {n}')

    if len(lines) >= 3:
        new_lines = lines[:2] + [lines[-1]] + lines[2:-1]
        new_content = ''.join(new_lines)
    else:
        print("Файл содержит меньше 3 строк, невозможно выполнить перестановку")
        new_content = content

with open('new_text18-7.txt', 'w', encoding=encoding) as file:
    file.write(new_content)
    print("Новый файл с переставленными строками создан: new_text18-7.txt")
