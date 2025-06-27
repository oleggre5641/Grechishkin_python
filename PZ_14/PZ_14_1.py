import re


def poisk_years(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Ищем год с последующим словом (год, года, году и т.д.)
    year_matches = re.findall(r'\b(1[0-9]{3}|20[0-9]{2})\s*(год[а-я]*|г\.)', text, re.IGNORECASE)
    
    # Форматируем результаты: объединяем число и слово
    years = [f"{num} {word}" for num, word in year_matches]

    print(f"Всего найдено годов: {len(years)}")
    print("Найденные годы:", ', '.join(years))


poisk_years("Dostoevsky.txt")
