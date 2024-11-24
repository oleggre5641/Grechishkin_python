# Дана непустая строка.
# Вывести коды ее первого и последнего символа

user_str = input("Введите строку: ")

# Обработка исключений
while len(user_str) < 1:
    try:
        a = user_str[0]
    except IndexError:
        print("Строка не должна быть пустой.")
        user_str = input("Введите строку: ")

# Получаем первый и последний символ, затем код каждого из них
first_char = user_str[0]
last_char = user_str[-1]

first_char_code = ord(first_char)
last_char_code = ord(last_char)

# Вывод результатов
print(f"Код первого символа '{first_char}': {first_char_code}")
print(f"Код последнего символа '{last_char}': {last_char_code}")
 
