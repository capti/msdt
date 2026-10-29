"""Проверки лабораторной работы 9: python test_table.py"""

from table import column_sums, diagonal_pattern, row_sums, transform

# Суммы строк и столбцов
matrix = [[1, 2, 3], [4, 5, 6]]
assert row_sums(matrix) == [6, 15]
assert column_sums(matrix) == [5, 7, 9]

# Матрица 1x1
assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]

# Одноколоночная матрица
matrix = [[1], [-1], [0]]
assert row_sums(matrix) == [1, -1, 0]
assert column_sums(matrix) == [0]

# Пустая матрица
assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []

# Диагональный узор размера 3
assert diagonal_pattern(3) == [
    [0, 1, 1],
    [2, 0, 1],
    [2, 2, 0],
]

# Индивидуальный вариант 11: чётные разделить на 2 целочисленно
control = [[-2, 0, 3], [4, -5, 6]]
assert transform(control) == [[-1, 0, 3], [2, -5, 3]]

# Исходная матрица не изменилась
result = transform(control)
result[0][0] = 100
assert control == [[-2, 0, 3], [4, -5, 6]]

# Суммы не изменяют матрицу
matrix = [[1, 2, 3], [4, 5, 6]]
row_sums(matrix)
column_sums(matrix)
diagonal_pattern(3)
assert matrix == [[1, 2, 3], [4, 5, 6]]

print("Все проверки пройдены")
