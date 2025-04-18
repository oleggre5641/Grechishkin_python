# Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов
# (путь), собственно имя и расширение. Выделить из этой строки расширение файла
# (без предшествующей точки).


# Пример для проверки
# example = "C:\Users\Oleg\Documents\music.mp3"
user_path = input("Введите полный путь до файла: ")

# Находим последний символ точки и выделяем часть строки после него
last_dot_index = user_path.rfind('.')

# Проверяем, нашли ли точку и не является ли она последним символом
if last_dot_index != -1 and last_dot_index < len(user_path) - 1:
    file_r = user_path[last_dot_index + 1:]  # Расширение файла
else:
    file_r = ""  # В случае отсутствия расширения

# Вывод результата
print(f"Расширение файла в последнем каталоге: {file_r}")
 
