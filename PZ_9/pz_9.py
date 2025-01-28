# Дана строка 'груша 45 991 63 100 12 морковь 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти минимальные продажи по
# каждому виду продукции, результаты вывести на экран.

data = 'груша 45 991 63 100 12 морковь 13 47 26 0 16'
dsp = data.split()
dsp_new = []

for el in dsp:
    try:
        el = int(el)
        dsp_new.append(el)
    except:
        dsp_new.append(el)

n = 1
first = {}
second = {}
fruit_names = []

for el in dsp:
    if el.isalpha():
        fruit_names.append(el)

first["Fruit"] = fruit_names[0]
second["Fruit"] = fruit_names[1]
first["Days"] = []
second["Days"] = []

dsp_new.remove(fruit_names[0])

for el in dsp_new:
    if type(el) is int:
        first["Days"].append(el)
    else:
        break

to_remove = first["Days"]
dsp_new.remove(fruit_names[1])
ostatok = []
for el in dsp_new:
    if el not in to_remove:
        ostatok.append(el)

for el in ostatok:
    if type(el) is int:
        second["Days"].append(el)
    else:
        break


print(first)
print(second)

def mini_slovar(slv):
    return min(slv["Days"])

print(f"Минимальная продажа за день {fruit_names[0]}: {mini_slovar(first)}")
print(f"Минимальная продажа за день {fruit_names[1]}: {mini_slovar(second)}")
