"""Работа с текстовыми файлами и проверка формата. Lab 10 (вариант 11)."""

import csv


def read_matrix(path):
    """Читает прямоугольную матрицу целых чисел из текстового файла UTF-8.

    Формат файла:
      - первая строка — два положительных целых числа: строки и столбцы;
      - затем ровно столько строк, в каждой ровно столько целых чисел.
    Лишние и пустые строки считаются ошибкой. Один обычный перевод строки
    после последней строки данных допустим.

    При неверном формате вызывается ValueError с пояснением и номером
    строки, где это применимо. Отсутствующий файл вызывает FileNotFoundError.
    """
    with open(path, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    if not lines:
        raise ValueError("Пустой файл: отсутствует заголовок")

    header = lines[0].split()
    if len(header) != 2:
        raise ValueError(
            f"Строка 1: заголовок должен содержать два числа, получено {lines[0]!r}"
        )
    try:
        rows = int(header[0])
        columns = int(header[1])
    except ValueError:
        raise ValueError(
            f"Строка 1: заголовок должен содержать целые числа, получено {lines[0]!r}"
        )
    if rows <= 0 or columns <= 0:
        raise ValueError(
            f"Строка 1: размеры должны быть положительными, получено {rows} и {columns}"
        )

    expected_lines = rows + 1
    if len(lines) > expected_lines:
        raise ValueError(
            f"Лишние строки: ожидалось {expected_lines}, получено {len(lines)}"
        )
    if len(lines) < expected_lines:
        raise ValueError(
            f"Недостаточно строк данных: ожидалось {rows}, получено {len(lines) - 1}"
        )

    matrix = []
    for index in range(rows):
        line_number = index + 2
        line = lines[index + 1]
        if not line.strip():
            raise ValueError(f"Строка {line_number}: пустая строка")
        parts = line.split()
        if len(parts) != columns:
            raise ValueError(
                f"Строка {line_number}: ожидалось {columns} чисел, получено {len(parts)}"
            )
        row = []
        for part in parts:
            try:
                row.append(int(part))
            except ValueError:
                raise ValueError(f"Строка {line_number}: нечисловая ячейка {part!r}")
        matrix.append(row)
    return matrix


def selected_sum(matrix):
    """Индивидуальный вариант 11: сумма элементов последнего столбца.

    Индексы начинаются с нуля. Для пустой матрицы результат 0.
    В матрице 1x1 последний столбец — единственный, элемент считается один раз.
    """
    if not matrix:
        return 0
    last_column = len(matrix[0]) - 1
    return sum(row[last_column] for row in matrix)


def export_csv(matrix, path):
    """Экспортирует матрицу в CSV стандартным модулем csv.

    Разбор CSV вручную через split(',') не используется: значения могут
    содержать разделители и кавычки, с которыми работает модуль csv.
    """
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(matrix)
