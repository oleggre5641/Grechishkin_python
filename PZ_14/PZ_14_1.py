# В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя
# (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту).
# Посчитать количество полученных элементов.

import re


def poisk_years(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    years = re.findall(r'\b(1[0-9]{3}|20[0-9]{2})\s*(?:год[а-я]*|г\.)', text, re.IGNORECASE)

    print(f"Всего найдено годов : {len(years)}")
    print("Найденные годы :", ', '.join(years))


poisk_years("Dostoevsky.txt")

