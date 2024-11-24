# Спортсмен-лыжник начал тренировки, пробежав в первый день 10 км. Каждый
# следующий день он увеличивал длину пробега на P процентов от пробега
# предыдущего дня (P — вещественное, 0< P <50). По данному P определить, после
# какого дня суммарный пробег лыжника за все дни превысит 200 км, и вывести
# найденное количество дней K (целое) и суммарный пробег S (вещественное число).


# Исходные данные
first_day_distance = 10.0

total_distance = 0.0
daily_distance = first_day_distance
day = 0
percent = input("Введите процент увеличения пробега (меньше 50%): ")

# Обработка исключений
while type(percent) != float:
    try:
        percent = float(percent)
        if percent > 50:
            1/0
    except ValueError and ZeroDivisionError:
        print("Неправильно ввели!")
        percent = input('Введите процент увеличения пробега (меньше 50%): ')

# Цикл до тех пор, пока суммарный пробег не превысит 200 км
while total_distance <= 200.0:
    total_distance += daily_distance
    day += 1
    daily_distance += daily_distance * (percent / 100)

# Выводим результат
print("Количество дней K:", day)
print("Суммарный пробег S:", total_distance)
 
