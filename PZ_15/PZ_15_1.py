import sqlite3

conn = sqlite3.connect('lekarstva.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS medicines")

cursor.execute('''
CREATE TABLE IF NOT EXISTS medicines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    usage TEXT,
    quantity INTEGER,
    price REAL,
    country TEXT
)
''')

medicines = [
    ('Аспирин', 'Головная боль, жар', 100, 50.99, 'Германия'),
    ('Парацетамол', 'Боль, жар', 150, 45.50, 'Россия'),
    ('Ибупрофен', 'Воспаление, боль', 80, 120.75, 'США'),
    ('Анальгин', 'Сильная боль', 60, 35.20, 'Россия'),
    ('Ношпа', 'Спазмы', 90, 85.60, 'Венгрия')
]

cursor.executemany('''
INSERT INTO medicines (name, usage, quantity, price, country)
VALUES (?, ?, ?, ?, ?)
''', medicines)

conn.commit()

print("База данных 'Аптека' успешно создана!")

# Примеры поиска и вывода информации
cursor.execute("SELECT * FROM medicines WHERE name LIKE 'А%'")
print("\nПрепараты на букву А : ")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT name, price FROM medicines WHERE country = 'Россия' AND price < 50")
print("\nРоссийские препараты дешевле 50 руб : ")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT name, quantity FROM medicines WHERE quantity > 80")
print("\nПрепараты которых больше 80 :")
for row in cursor.fetchall():
    print(row)

# Примеры удаления информации из базы данных
#
# cursor.execute("DELETE FROM medicines WHERE id = 3")
# print("Удален препарат с ID 3 ")
#
# cursor.execute("DELETE FROM medicines WHERE country = 'США'")
# print("Удалены все препараты США")
#
# cursor.execute("DELETE FROM medicines WHERE quantity < 70")
# print("Удалены препараты с количеством меньшк 70")
#
# conn.commit()

# Примеры редактирования информации в базе даных
#
# cursor.execute("UPDATE medicines SET price = 10.00 WHERE name = 'Аспирин'")
# print("Изменена цена Аспирина на 10 руб")
#
# cursor.execute("UPDATE medicines SET price = price * 5 WHERE country = 'Россия'")
# print("Цены российских препаратов увеличены на 50%")
#
# cursor.execute("UPDATE medicines SET quantity = quantity + 20 WHERE price > 100")
# print("Количество дорогих препаратов увеличено на 20")
#
# conn.commit()


print("\n")
cursor.execute("SELECT * FROM medicines")
for row in cursor.fetchall():
    print(row)

conn.close()
