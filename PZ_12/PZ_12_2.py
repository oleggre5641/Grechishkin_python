# Составить генератор (yield), который преобразует
# все буквенные символы в строчные.

def lowercase(tekst):
    for a in tekst:
        yield a.lower()

txt = input("Введите текст : ")
result = ''.join(lowercase(txt))
print("Результат : ", result)
