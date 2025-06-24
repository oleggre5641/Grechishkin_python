# Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
# Добавьте методы для сложения, вычитания и умножения матриц.


class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data:
            self.data = data
        else:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одного размера")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for x in range(self.cols):
                result.data[i][x] = self.data[i][x] + other.data[i][x]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одного размера")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for m in range(self.cols):
                result.data[i][m] = self.data[i][m] - other.data[i][m]
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for o in range(self.cols):
                    result.data[i][o] = self.data[i][o] * other
            return result
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Количество столцов первой матрицы должно равняться количеству строк второй")
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for w in range(other.cols):
                    for k in range(self.cols):
                        result.data[i][w] += self.data[i][k] * other.data[k][w]
            return result
        else:
            raise TypeError("Неподдерживаемый тип данных (можно только числа, или попробуй число поменьше)")


# m1 = Matrix(2, 2, [[1, 2], [3, 4]])
# m2 = Matrix(2, 2, [[5, 6], [7, 8]])
#
# print("Матрица 1:")
# print(m1)
# print("\nМатрица 2:")
# print(m2)
#
# print("\nСложение:")
# print(m1 + m2)
#
# print("\nВычитание:")
# print(m1 - m2)
#
# print("\nУмножение матриц:")
# print(m1 * m2)
#
# print("\nУмножение на число:")
# print(m1 * 2)

