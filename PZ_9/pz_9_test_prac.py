inp = int(input("Введите целое число: "))

temp = []

while inp > 0:
    digit = inp % 10
    digit_kvadrat = digit ** 2
    temp.append(str(digit_kvadrat))
    inp = inp // 10

temp.reverse()

print("".join(temp))
