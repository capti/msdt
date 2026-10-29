"""Обработка прямоугольных таблиц (вложенных списков). Lab 9.

Все функции не изменяют полученную матрицу и не выполняют ввод-вывод.
"""


def row_sums(matrix):
    """Возвращает список сумм строк матрицы. Для [] возвращает []."""
    return [sum(row) for row in matrix]


def column_sums(matrix):
    """Возвращает список сумм столбцов матрицы. Для [] возвращает [].

    Непустая матрица прямоугольная и имеет хотя бы один столбец.
    """
    if not matrix:
        return []
    return [sum(row[column] for row in matrix) for column in range(len(matrix[0]))]


def diagonal_pattern(size):
    """Создаёт квадратную таблицу размера size x size.

    На главной диагонали 0, выше неё 1, ниже неё 2. size >= 1.
    """
    matrix = [[0] * size for _ in range(size)]
    for row in range(size):
        for column in range(size):
            if row == column:
                matrix[row][column] = 0
            elif row < column:
                matrix[row][column] = 1
            else:
                matrix[row][column] = 2
    return matrix


def transform(matrix):
    """Индивидуальный вариант 11: чётные разделить на 2 целочисленно.

    Возвращает новую матрицу той же формы, исходная не изменяется.
    Для [] результат — [].
    """
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            if value % 2 == 0:
                new_row.append(value // 2)
            else:
                new_row.append(value)
        result.append(new_row)
    return result
