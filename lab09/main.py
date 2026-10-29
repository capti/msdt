"""Ввод-вывод для лабораторной работы 9 (таблицы и вложенные списки)."""

from table import column_sums, diagonal_pattern, row_sums, transform


def input_matrix():
    """Запрашивает размеры и читает прямоугольную матрицу с проверкой строк."""
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    matrix = []
    for _ in range(rows):
        row = [int(part) for part in input("Строка таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)
    return matrix


def main():
    matrix = input_matrix()

    print("Исходная матрица:")
    for row in matrix:
        print(*row)

    print("Суммы строк:", row_sums(matrix))
    print("Суммы столбцов:", column_sums(matrix))

    size = int(input("Положительный размер узора: "))
    while size < 1:
        print("Размер должен быть положительным")
        size = int(input("Повторите размер: "))
    print(f"Диагональный узор размера {size}:")
    for row in diagonal_pattern(size):
        print(*row)

    print("Результат преобразования (вариант 11: чётные разделить на 2):")
    for row in transform(matrix):
        print(*row)


if __name__ == "__main__":
    main()
